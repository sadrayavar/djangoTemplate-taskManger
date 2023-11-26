from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("account/", views.account, name="account"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="loginUser",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="allTasks"),
        name="logoutUser",
    ),
    path("register/", views.registerUser, name="registerUser"),
]
