from import_export import resources
from .models import Ingredients, Tags, Recipe, ShoppingCart


class ReportResourceIngredients(resources.ModelResource):
    class Meta:
        model = Ingredients


class ReportResourceTags(resources.ModelResource):
    class Meta:
        model = Tags


class ReportResourceRecipe(resources.ModelResource):
    class Meta:
        model = Recipe


class ReportResourceShoppingCart(resources.ModelResource):
    class Meta:
        model = ShoppingCart
