from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LENGTH_NAME = 150
MAX_LENGTH_CODE = 255
MAX_LENGTH_ROLE = 10
MAX_LENGTH_EMAIL = 254
USER_ROLE = "user"
ADMIN_ROLE = "admin"
USERS_ROLE = (
    (USER_ROLE, "Пользователь"),
    (ADMIN_ROLE, "Администратор"),
)


class User(AbstractUser):
    username = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
        blank=False,
        unique=True,
        verbose_name="Емаил",
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name="Фамилия",
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=MAX_LENGTH_ROLE,
        choices=USERS_ROLE,
        default=USER_ROLE,
        verbose_name="Роль",
        blank=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    @property
    def is_user(self):
        return self.role == USER_ROLE

    @property
    def is_admin(self):
        return self.is_superuser or self.role == ADMIN_ROLE
