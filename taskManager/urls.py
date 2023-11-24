from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homePage, name="homePage"),
    path("user/", include("user.urls"), name="userPage"),
    path("task/", include("task.urls"), name="taskPage"),
]
