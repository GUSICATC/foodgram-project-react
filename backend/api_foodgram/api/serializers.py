from rest_framework import serializers
from users.models import MAX_LENGTH_EMAIL, MAX_LENGTH_NAME, User
from recipes.models import Tags, Recipe
import base64
import webcolors
from django.core.files.base import ContentFile
import re


class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_username(self, value):
        if re.fullmatch(r"^[\w.@+-]+\Z", value):
            return value
        raise serializers.ValidationError(
            "Невозможно создать пользователя с таким набором симвлолов"
        )


class TagsSerializer(serializers.ModelSerializer):
    color = Hex2NameColor()

    class Meta:
        model = Tags
        fields = (
            'id',
            "name",
            'color',
            'slug',
        )


class RecipeSerializer(serializers.ModelSerializer):

    image = Base64ImageField(required=False, allow_null=True)
    # tags = serializers.PrimaryKeyRelatedField(queryset=Tags.objects.all())
    # is_favorited = serializers.SerializerMethodField('get_favorited')
    # # is_in_shopping_cart = serializers.SerializerMethodField(
    # #   'get_shopping_cart')

    class Meta:
        model = Recipe

        fields = (
            'id',
            "tags",
            'author',
            'ingredients',
            # 'is_favorited',
            # 'is_in_shopping_cart',
            'image',
            'name',
            'text',
            'cooking_time',
        )

    def create(self, validated_data):

        author = self.context['request'].user
        recipe = Recipe.objects.create(author=author, **validated_data)

        return recipe
    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get("id", instance.id)
    #     instance.tags = validated_data.get("tags", instance.tags)
    #     instance.author = validated_data.get("author", instance.author)
    #     instance.ingredients = validated_data.get(
    #         "ingredients", instance.ingredients)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.text = validated_data.get("text", instance.text)
    #     instance.cooking_time = validated_data.get(
    #         "cooking_time", instance.cooking_time)
    #     instance.save()
    #     return instance

    # def get_favorited(self, request):
    #     return False

    # def get_is_in_shopping_cart(self, obj):
    #     if self.context.get(
    #         'request'
    #     ) is None or self.context.get('request').user.is_anonymous:
    #         return False
    #     return ShoppingCart.objects.filter(
    #         recipe=obj,
    #         user=self.context.get('request').user
    #     ).exists()


class FavoriteSerializer(serializers.ModelSerializer):
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
