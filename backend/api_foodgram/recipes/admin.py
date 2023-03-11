from django.contrib import admin
from recipes.models import Tags, Recipe
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .resource import ReportResourceIngredients, ReportResourceTags, ReportResourceRecipe
from .models import Ingredients, IngredientsAmount


class AmountInline(admin.TabularInline):
    model = IngredientsAmount
    extra = 1


class IngredientsAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceIngredients
    search_fields = ("name",)


admin.site.register(Ingredients, IngredientsAdmin)


class RecipeAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceRecipe
    inlines = (AmountInline),
    list_display = (
        'author',
        'name',
        'image',
        'text',
        'cooking_time',

    )
    filter_horizontal = ('tags', 'favorit', 'in_shopping_cart')
    search_fields = ("author",)


admin.site.register(Recipe, RecipeAdmin)


@admin.register(Tags)
class TagsAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceTags
    list_display = (
        "name",
        'color',
        'slug',
    )
    search_fields = ("name",)
