from django.urls import path
from . import views
from django.contrib.auth import views as authView
from taskManager.constant import tabs, profileTitles, logo

urlpatterns = [
    path("profile/", views.editUser, name="profilePage"),
    path("login/", views.loginUser, name="loginUser"),
    path(
        "logout/",
        authView.LogoutView.as_view(next_page="homePage"),
        name="logoutUserPage",
    ),
    path("register/", views.registerUser, name="registerUserPage"),
    path("delete/", views.deleteUser, name="deleteUserPage"),  # type: ignore
]
