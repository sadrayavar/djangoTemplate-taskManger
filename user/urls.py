from django.urls import path
from . import views

urlpatterns = [
    path("", views.user),
    path("login/", views.loginUser, name="loginUser"),
    path("register/", views.registerUser, name="registerUser"),
]
