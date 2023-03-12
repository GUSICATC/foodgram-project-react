from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Follow


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "role",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "auth_token",
    )


admin.site.register(User, CustomUserAdmin)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'following',

    )
