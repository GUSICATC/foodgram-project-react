from datetime import datetime as dt

from api.custom_filters import TagsFilter
from api.pagination import LimitPageNumberPagination
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from api.serializers import (FollowSerializer, IngredientSerializer,
                             RecipeSerializer, TagSerializer)
from api_foodgram.settings import DATE_TIME_FORMAT
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from recipes.models import Ingredient, Recipe, Tag
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from users.models import Follow, User


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("^name",)
    pagination_class = None


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = LimitPageNumberPagination
    permission_classes = (IsOwnerOrReadOnly,)
    filterset_class = TagsFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        methods=[
            "post",
            "delete",
        ],
        detail=True,
    )
    def favorite(self, request, pk=None):
        recipe = get_object_or_404(Recipe, pk=pk)

        if request.method == "POST":
            if recipe.is_favorited.filter(id=request.user.id).exists():
                return Response({"ошибка рицепт уже в избранном"})
            recipe.is_favorited.add(request.user)
            return Response({"добавлен в избранное"})

        recipe.is_favorited.remove(request.user)
        return Response({"удален из избранного"})

    @action(
        methods=[
            "post",
            "delete",
        ],
        detail=True,
    )
    def shopping_cart(self, request, pk=None):
        recipe = get_object_or_404(Recipe, pk=pk)

        if request.method == "POST":
            if recipe.is_in_shopping_cart.filter(id=request.user.id).exists():
                return Response({"ошибка рицепт уже в корзине"})
            recipe.is_in_shopping_cart.add(request.user)
            return Response({"добавлен в корзину"})

        recipe.is_in_shopping_cart.remove(request.user)
        return Response({"удален из корзины"})

    @action(methods=("get",), detail=False)
    def download_shopping_cart(self, request: WSGIRequest):
        user = self.request.user
        if not user.carts.exists():
            return Response(status=HTTP_400_BAD_REQUEST)

        filename = f"{user.username}_shopping_list.txt"
        shopping_list = [
            f"Список покупок для:\n\n{user.first_name}\n"
            f"{dt.now().strftime(DATE_TIME_FORMAT)}\n"
        ]

        ingredients = (
            Ingredient.objects.filter(recipe__recipe__in_carts__user=user)
            .values("name", measurement=F("measurement_unit"))
            .annotate(amount=Sum("recipe__amount"))
        )

        for ing in ingredients:
            shopping_list.append(
                f'{ing["name"]}: {ing["amount"]} {ing["measurement"]}'
            )
        shopping_list = "\n".join(shopping_list)
        response = HttpResponse(
            shopping_list, content_type="text.txt; charset=utf-8"
        )
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response


class SubscriptionsViewSet(UserViewSet):
    pagination_class = LimitPageNumberPagination
    queryset = User.objects.all()

    @action(
        methods=["post"],
        detail=True,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, pk=id)

        if user == author:
            return Response(
                {"errors": "Вы не можете подписываться на самого себя"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if Follow.objects.filter(user=user, author=author).exists():
            return Response(
                {"errors": "Вы уже подписаны на данного пользователя"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        follow = Follow.objects.create(user=user, author=author)
        serializer = FollowSerializer(follow, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def del_subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        if user == author:
            return Response(
                {"errors": "Вы не можете отписываться от самого себя"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        follow = Follow.objects.filter(user=user, author=author)
        if follow.exists():
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {"errors": "Вы уже отписались"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages, many=True, context={"request": request}
        )
        return self.get_paginated_response(serializer.data)
