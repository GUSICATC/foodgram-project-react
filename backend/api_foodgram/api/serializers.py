import re

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from users.models import MAX_LENGTH_EMAIL, MAX_LENGTH_NAME, User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=MAX_LENGTH_NAME)
    email = serializers.EmailField(max_length=MAX_LENGTH_EMAIL)

    class Meta:
        model = User
        fields = ("username", "email")

    def validate_username(self, value):
        name = value.lower()
        if name == "me" and re.fullmatch(r"^[\w.@+-]+\Z", value):
            return value
        raise serializers.ValidationError(
            "Невозможно создать пользователя с таким набором симвлолов"
        )

    def validate(self, data):
        if not ("username" or "email") in data:
            raise serializers.ValidationError("Нет обязательных ключей")
        username = data["username"]
        email = data["email"]
        if User.objects.filter(**data).exists() or (
            not User.objects.filter(username=username).exists()
            and not User.objects.filter(email=email).exists()
        ):
            return data
        raise serializers.ValidationError(
            "Невозможно создать пользователя с такими значениями"
            '"username" и "email"'
        )


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=MAX_LENGTH_NAME)

    class Meta:
        model = User
        fields = ("username", "confirmation_code")

    def validate(self, data):
        user = get_object_or_404(User, username=data["username"])
        if user.confirmation_code != data["confirmation_code"]:
            raise serializers.ValidationError("Код подтверждения не верен")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
