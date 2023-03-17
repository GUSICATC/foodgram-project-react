from import_export import resources
from .models import Ingredient, Tag, Recipe, ShoppingCart


class ReportResourceIngredients(resources.ModelResource):
    class Meta:
        model = Ingredient


class ReportResourceTags(resources.ModelResource):
    class Meta:
        model = Tag


class ReportResourceRecipe(resources.ModelResource):
    class Meta:
        model = Recipe


class ReportResourceShoppingCart(resources.ModelResource):
    class Meta:
        model = ShoppingCart
