from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from users.models import User

MAX_LENGTH_FOR_CHARFIELD: int = 256
MAX_LENGTH_FOR_SLUG: int = 50


class Category(models.Model):
    name = models.CharField(
        "Название категории",
        max_length=MAX_LENGTH_FOR_CHARFIELD,
    )
    slug = models.SlugField(
        unique=True,
        max_length=MAX_LENGTH_FOR_SLUG,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name