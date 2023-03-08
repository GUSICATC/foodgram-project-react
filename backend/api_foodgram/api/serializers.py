from rest_framework import serializers
from users.models import MAX_LENGTH_EMAIL, MAX_LENGTH_NAME, User
from recipes.models import Tags, Recipe
import base64  # Модуль с функциями кодирования и декодирования base64
import webcolors
from django.core.files.base import ContentFile
import re


class Hex2NameColor(serializers.Field):
    # При чтении данных ничего не меняем - просто возвращаем как есть
    def to_representation(self, value):
        return value
    # При записи код цвета конвертируется в его название

    def to_internal_value(self, data):
        # Доверяй, но проверяй
        try:
            # Если имя цвета существует, то конвертируем код в название
            data = webcolors.hex_to_name(data)
        except ValueError:
            # Иначе возвращаем ошибку
            raise serializers.ValidationError('Для этого цвета нет имени')
        # Возвращаем данные в новом формате
        return data


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Если полученный объект строка, и эта строка
        # начинается с 'data:image'...
        if isinstance(data, str) and data.startswith('data:image'):
            # ...начинаем декодировать изображение из base64.
            # Сначала нужно разделить строку на части.
            format, imgstr = data.split(';base64,')
            # И извлечь расширение файла.
            ext = format.split('/')[-1]
            # Затем декодировать сами данные и поместить результат в файл,
            # которому дать название по шаблону.
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

        )

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
    author = UserSerializer(read_only=True)
    image = Base64ImageField(required=False, allow_null=True)
    is_favorited = serializers.SerializerMethodField('get_favorited')
    # is_in_shopping_cart = serializers.SerializerMethodField(
    #   'get_shopping_cart')

    class Meta:
        model = Recipe
        depth = 1
        fields = (
            'id',
            "tags",
            'author',
            'ingredients',
            'is_favorited',
            # 'is_in_shopping_cart',
            'image',
            'name',
            'text',
            'cooking_time',
        )

    def get_favorited(self, request):
        return False

    #  def get_is_in_shopping_cart(self, obj):
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
