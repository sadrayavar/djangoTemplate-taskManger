from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminHomePage, name="adminPage"),
    path("hide_commmment/<int:commentId>", views.hideComment, name="hideComment"),
    path("approve_task/<int:taskId>", views.approveTask, name="approveTask"),
]
