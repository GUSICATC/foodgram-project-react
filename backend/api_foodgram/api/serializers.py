import re


from django.shortcuts import get_object_or_404
from rest_framework import serializers
from users.models import MAX_LENGTH_EMAIL, MAX_LENGTH_NAME, User
from recipes.models import Tags, Recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",

        )


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = (
            'id',
            "name",
            'color',
            'slug',
        )


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            "tags",
            'author',
            'ingredients',
            'image',
            'name',
            'text',
            'cooking_time',
        )
        depth = 1
