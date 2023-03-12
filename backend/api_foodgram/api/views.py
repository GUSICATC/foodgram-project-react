from users.models import User, Follow
from recipes.models import Tags, Recipe, Ingredients
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (UserSerializer,
                          TagsSerializer,
                          RecipeSerializer,
                          IngredientsSerializer, FollowSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, filters, mixins
from rest_framework.decorators import action
from .custom_filters import TagsFilter


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = None


class TagsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)
    filterset_class = TagsFilter

    @action(methods=['post', 'delete',], detail=True)
    def favorite(self, request, id=None):
        recipe = get_object_or_404(Recipe, id=id)

        if request.method == 'POST':
            if recipe.is_favorited.filter(id=request.user.id).exists():
                return Response({'ошибка рицепт уже в избранном'})
            recipe.is_favorited.add(request.user)
            return Response({'добавлен в избранное'})

        recipe.is_favorited.remove(request.user)
        return Response({'удален из избранного'})

    @action(methods=['post', 'delete',], detail=True)
    def shopping_cart(self, request, id=None):
        recipe = get_object_or_404(Recipe, id=id)

        if request.method == 'POST':
            if recipe.is_in_shopping_cart.filter(id=request.user.id).exists():
                return Response({'ошибка рицепт уже в корзине'})
            recipe.is_in_shopping_cart.add(request.user)
            return Response({'добавлен в корзину'})

        recipe.is_in_shopping_cart.remove(request.user)
        return Response({'удален из корзины'})


class SubscriptionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user.id
        follow = User.objects.all()
        return follow.filter(following__user_id=user)
