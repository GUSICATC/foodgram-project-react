import uuid


from .serializers import (TagsSerializer, RecipeSerializer)


from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from recipes.models import Tags, Recipe
from users.models import User


class TagsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ('tag',)


class RecipeViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ('tag',)
