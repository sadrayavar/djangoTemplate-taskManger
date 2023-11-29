from django.urls import path
from . import views
from django.contrib.auth import views as authView
from taskManager.constant import tabs, profileTitles, logo

urlpatterns = [
    path("profile/", views.account, name="profilePage"),
    path(
        "login/",
        authView.LoginView.as_view(
            template_name="login.html",
            extra_context={"tabs": tabs, "title": profileTitles["login"], "logo": logo},
            redirect_authenticated_user=True,
        ),
        name="loginUser",
    ),
    path(
        "logout/",
        authView.LogoutView.as_view(next_page="explorePage"),
        name="logoutUser",
    ),
    path("register/", views.registerUser, name="registerUser"),
]
