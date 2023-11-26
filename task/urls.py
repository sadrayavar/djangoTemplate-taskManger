from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.allTasks, name="allTasks"),
    path("myTasks/", views.userTasks, name="userTasks"),
    path("<int:taskId>/", views.singleTask, name="singleTask"),
    path("<int:taskId>/delete", views.deleteTask, name="deleteTask"),
    path("<int:taskId>/edit", views.editTask, name="editTask"),  # type: ignore
    path("add/", views.addTask, name="addTask"),
]
