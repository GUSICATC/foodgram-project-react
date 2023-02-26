from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "role",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "confirmation_code",
    )


admin.site.register(User, CustomUserAdmin)
