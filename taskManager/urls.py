from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="userProfile"),
    path("", include("task.urls"), name="allTasks"),
    path("account/", include("user.urls"), name="userPage"),
]
