from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task.urls"),name="taskList"),
    path("account/", include("user.urls"), name="userPage"),
]
