from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TagsViewSet, RecipeViewSet
router = DefaultRouter()
router.register(r"tags", TagsViewSet, basename="tags")
router.register(r"recipes", RecipeViewSet, basename="recipes")
# router.register(r"users/subscriptions/",
#                 SubscriptionsViewSet, basename="users")
# router.register(r"ingredients", IngredientsViewSet, basename="users")


# router.register(r"recipes/(?P<recipes_id>\d+)/shopping_cart/",
#                 FavoriteViewSet, basename="tags")
# router.register(r"recipes/(?P<recipes_id>\d+)/favorite/",
#                 FavoriteViewSet, basename="tags")
# router.register(r"recipes/download_shopping_cart/",
#                 RecipeViewSet, basename="recipes")


urlpatterns = [


    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("", include(router.urls)),
]
