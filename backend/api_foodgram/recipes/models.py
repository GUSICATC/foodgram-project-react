from django.core.validators import MinValueValidator
from django.db import models
from users.models import User

MAX_LENGTH_FOR_CHARFIELD: int = 200
MAX_LENGTH_FOR_SLUG: int = 50


class Tag(models.Model):
    BLUE = "#0000FF"
    ORANGE = "#FFA500"
    GREEN = "#008000"
    PURPLE = "#800080"
    YELLOW = "#FFFF00"

    COLOR_CHOICES = [
        (BLUE, "Синий"),
        (ORANGE, "Оранжевый"),
        (GREEN, "Зеленый"),
        (PURPLE, "Фиолетовый"),
        (YELLOW, "Желтый"),
    ]
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название тега"
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        choices=COLOR_CHOICES,
        verbose_name="Цвет в HEX",
    )
    slug = models.SlugField(
        max_length=200, unique=True, verbose_name="Уникальный слаг"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Название ингредиента"
    )

    measurement_unit = models.CharField(
        max_length=200, verbose_name="Единица измерения"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "ингридиент"
        verbose_name_plural = "ингридиенты"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "measurement_unit"], name="unique ingredient"
            )
        ]

    def __str__(self):
        return f"{self.name} {self.measurement_unit}"


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe",
        verbose_name="Автор рецепта",
    )
    name = models.CharField(max_length=200, verbose_name="Название рецепта")

    image = models.ImageField(
        upload_to="recipes/", verbose_name="Картинка рецепта"
    )

    text = models.TextField(
        verbose_name="Описание рецепта", help_text="Описание"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientAmount",
        verbose_name="Ингридиенты",
        related_name="recipes",
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="recipes",
        verbose_name="Тег",
    )
    cooking_time = models.IntegerField(
        "Время приготовления (в минутах)",
        default=1,
        validators=(
            MinValueValidator(
                1,
                message=("Минимальное время приготовления 1 минута"),
            ),
        ),
    )

    is_favorited = models.ManyToManyField(
        User,
        through="Favorit",
        related_name="favorited",
        default=None,
        blank=True,
    )
    is_in_shopping_cart = models.ManyToManyField(
        User,
        through="ShoppingCart",
        related_name="in_shopping_cart",
        default=None,
        blank=True,
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return f"{self.name}. Автор: {self.author.username}"


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe",
        verbose_name="Ингридиент",
    )
    amount = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(
                1, message="Минимальное количество ингридиентов 1"
            ),
        ),
        verbose_name="Количество",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Количество ингридиента"
        verbose_name_plural = "Количество ингридиентов"
        constraints = [
            models.UniqueConstraint(
                fields=["ingredient", "recipe"],
                name="unique ingredients recipe",
            )
        ]

    def __str__(self) -> str:
        return f"{self.amount} {self.ingredient}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="carts"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="in_carts",
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique shopping chart"
            )
        ]

    def __str__(self):
        return f"{self.user} {self.recipe}"


class Favorit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Рецепт",
    )

    class Meta:
        verbose_name = "Избранный рецепт"
        verbose_name_plural = "Избранные рецепты"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "recipe",
                    "user",
                ),
                name="recipe is favorite alredy",
            ),
        )

    def __str__(self):
        return f"{self.user} {self.recipe}"
