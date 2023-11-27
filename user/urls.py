from django.urls import path
from . import views
from django.contrib.auth import views as authView

urlpatterns = [
    path("profile/", views.account, name="account"),
    path(
        "login/",
        authView.LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="loginUser",
    ),
    path(
        "logout/",
        authView.LogoutView.as_view(next_page="allTasks"),
        name="logoutUser",
    ),
    path("register/", views.registerUser, name="registerUser"),
]
