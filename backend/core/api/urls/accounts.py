from django.urls import path
from api.views import AuthViewSet

urlpatterns = [
    path("register/", AuthViewSet.as_view({"post": "register"}), name="register"),
    path("login/", AuthViewSet.as_view({"post": "login"}), name="login"),
]