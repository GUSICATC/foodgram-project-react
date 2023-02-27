from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (get_token, UserViewSet, RecipeViewSet,
                       signup)

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")
router.register(r"users/subscriptions/", UserViewSet, basename="users")
router.register(r"users/(?P<users_id>\d+)/subscriptions/",
                UserViewSet, basename="users")
router.register(r"ingredients", UserViewSet, basename="users")
router.register(r"ingredients/(?P<ingredients_id>\d+)/",
                UserViewSet, basename="users")
router.register(r"tags", UserViewSet, basename="tags")
router.register(r"tags/(?P<tags_id>\d+)/", UserViewSet, basename="tags")
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"recipes/(?P<recipes_id>\d+)",
                RecipeViewSet, basename="recipes")
router.register(r"recipes/(?P<recipes_id>\d+)/shopping_cart/",
                FavoriteViewSet, basename="tags")
router.register(r"recipes/(?P<recipes_id>\d+)/favorite/",
                FavoriteViewSet, basename="tags")
router.register(r"recipes/download_shopping_cart/",
                RecipeViewSet, basename="recipes")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/signup/", signup, name="signup"),
    path("auth/token/", get_token, name="get_token"),
]
