from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (get_token, UserViewSet,
                       signup)

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/signup/", signup, name="signup"),
    path("auth/token/", get_token, name="get_token"),
]
