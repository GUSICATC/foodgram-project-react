from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
MAX_LENGTH_FOR_CHARFIELD: int = 200
MAX_LENGTH_FOR_SLUG: int = 50
CHOICES = (
    ('KG', 'кг'),
    ('GR', 'гр.'),
    ('ML', 'мл'),
)


class Tags(models.Model):
    name = models.CharField(
        "Тег",
        max_length=MAX_LENGTH_FOR_CHARFIELD, unique=True, blank=True,
    )
    color = models.CharField('Цвет',
                             max_length=MAX_LENGTH_FOR_CHARFIELD, unique=True, blank=True,
                             )
    slug = models.SlugField('Слаг',
                            max_length=MAX_LENGTH_FOR_SLUG, unique=True, blank=True,
                            )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(
        'Название ингридиента',
        max_length=MAX_LENGTH_FOR_CHARFIELD, blank=True,)
    amount = models.FloatField(
        'количество', max_length=5, default=0, blank=True,)
    measurement_unit = models.CharField(
        'единица измерения', choices=CHOICES, max_length=MAX_LENGTH_FOR_CHARFIELD, blank=True,)

    class Meta:
        verbose_name = "ингридиент"
        verbose_name_plural = "ингридиенты"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE,
                             related_name='teg',
                             verbose_name='Тег',
                             null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="автор",
        null=True,
    )
    ingredients = models.ForeignKey(Ingredients,
                                    on_delete=models.CASCADE,
                                    related_name='ingredients',
                                    verbose_name='ингридиент',
                                    null=True)
    favorit = models.ManyToManyField(
        User, related_name="favorit", default=None, blank=True,)
    in_shopping_cart = models.ManyToManyField(
        User, related_name="in_shopping_cart", default=None, blank=True,)
    name = models.CharField(
        "Название",
        max_length=MAX_LENGTH_FOR_CHARFIELD,
    )
    image = models.ImageField(
        'Картинка',

        blank=True
    )
    text = models.TextField(
        verbose_name="Описание",
        help_text='Описание'
    )
    cooking_time = models.IntegerField('Время приготовления (в минутах)', default=1,
                                       validators=[
                                           MinValueValidator(1)
                                       ]
                                       )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("name",)

    def __str__(self):
        return self.name
