from django.contrib import admin
from recipes.models import Tags, Recipe, Ingredients


@admin.register(Tags)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "name",
        'color',
        'slug',
    )
    search_fields = ("name",)


@admin.register(Recipe)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'ingredients',
        'author',
        "tags",
        'image',
        'name',
        'text',
        'cooking_time',

    )
    search_fields = ("name",)


@admin.register(Ingredients)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit',
    )
    search_fields = ("name",)
