from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        unique=True,
        verbose_name="Емаил",
    )
    first_name = models.CharField(
        max_length=150, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
        blank=True,
        null=True,
    )
    is_subscribed = models.BooleanField('подписка', default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        null=True)
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписка',
        null=True,)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
