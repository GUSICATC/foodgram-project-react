from api.views import (IngredientsViewSet, RecipeViewSet, SubscriptionsViewSet,
                       TagsViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"
router = DefaultRouter(trailing_slash=True)
router.register(r"tags", TagsViewSet, basename="tags")
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients"),
router.register(r"users", SubscriptionsViewSet, basename="subscriptions"),
urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
