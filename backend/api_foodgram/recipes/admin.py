from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from recipes.models import (Favorit, Ingredient, IngredientAmount, Recipe,
                            ShoppingCart, Tag)
from recipes.resource import (ReportResourceIngredients, ReportResourceRecipe,
                              ReportResourceTags)


class AmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


class IngredientsAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceIngredients
    search_fields = ("name",)


admin.site.register(Ingredient, IngredientsAdmin)


class RecipeAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceRecipe
    inlines = ((AmountInline),)
    list_display = (
        "author",
        "name",
        "image",
        "text",
        "cooking_time",
    )
    filter_horizontal = ("tags",)
    search_fields = ("author",)


admin.site.register(Recipe, RecipeAdmin)


@admin.register(Tag)
class TagsAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceTags
    list_display = (
        "name",
        "color",
        "slug",
    )
    search_fields = ("name",)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )


@admin.register(Favorit)
class FavoritAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
