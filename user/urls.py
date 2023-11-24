from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="loginUser"),
    path("register/", views.registerUser, name="registerUser"),
    path("edit/", views.editUser, name="editUser"),
    path("delete/", views.deleteUser, name="deleteUser"),
]
