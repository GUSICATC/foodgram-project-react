import uuid
from rest_framework.decorators import api_view

from .serializers import (TagsSerializer, RecipeSerializer, FavoriteSerializer)

from django.shortcuts import get_object_or_404
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
     
    @action(methods=['post', 'delete',], detail=True)
    def favorite(self, request, id=None):
        recipe = get_object_or_404(Recipe, id=id)

        if request.method == 'POST':
            if recipe.favorite.filter(id=request.user.id).exists():
                return Response({'ошибка рицепт уже в избранном'})
            recipe.favorite.add(request.user)
            return Response({'добавлен в любимые'})

        recipe.favorite.remove(request.user)
        return Response({'удален из любимых'})


class SubscriptionsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('tag',)

    @action(methods=['get', 'delete',], detail=True)
    def subscribe(self, request, id=None):
        recipe = get_object_or_404(Recipe, id=id)

        if request.method == 'POST':
            if recipe.favorited.filter(id=request.user.id).exists():
                return Response({'ошибка рицепт уже в избранном'})
            recipe.favorited.add(request.user)
            return Response({'добавлен в любимые'})

        recipe.favorited.remove(request.user)
        return Response({'удален из любимых'})

    @action(methods=['get', 'delete',], detail=True)
    def subscriptions(self, request, id=None):
        recipe = get_object_or_404(Recipe, id=id)
