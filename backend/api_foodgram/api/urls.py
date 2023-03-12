from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TagsViewSet, RecipeViewSet, IngredientsViewSet, SubscriptionsViewSet


router = DefaultRouter(trailing_slash=True)
router.register(r"tags", TagsViewSet, basename="tags")
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients"),
router.register(r"users/subscriptions", SubscriptionsViewSet,
                basename="subscriptions"),


#

# router.register(r"recipes/download_shopping_cart/",
#                 RecipeViewSet, basename="recipes")


urlpatterns = [

    path("", include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


    # path('recipes/download_shopping_cart/', download_shopping_cart)

]
# print(router.urls)
