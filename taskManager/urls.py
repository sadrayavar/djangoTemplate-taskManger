from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task.urls"), name="homePage"),
    path("account/", include("user.urls"), name="userPage"),
]
