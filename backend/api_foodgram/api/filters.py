from django_filters.rest_framework import CharFilter, FilterSet
from recipes.models import Recipe


class TagsFilter(FilterSet):
    tags = CharFilter(field_name="tags__slug")

    class Meta:
        model = Recipe
        fields = ('author', 'name',
                  'is_favorited',
                  'is_in_shopping_cart',
                  'tags'
                  )
