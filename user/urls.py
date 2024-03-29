from django.urls import path
from . import views
from django.contrib.auth import views as authView
from taskManager.constant import tabs, profileTitles, logo

urlpatterns = [
    path("", views.editUser, name="profilePage"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logoutUser, name="logoutUserPage"),
    path("register/", views.registerUser, name="registerUserPage"),
    path("delete/", views.deleteUser, name="deleteUserPage"),
]
