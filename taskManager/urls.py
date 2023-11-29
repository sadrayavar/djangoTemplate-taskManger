from django.contrib import admin
from django.urls import path, include
from comment.views import myComments

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task.urls")),
    path("account/", include("user.urls")),
    path("comments/", myComments, name="myCommentsPage"),
]
