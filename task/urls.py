from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.taskList, name="taskList"),
    path("<int:taskId>/", views.singleTask, name="singleTask"),
    path("<int:taskId>/delete", views.deleteTask, name="deleteTask"),
    path("<int:taskId>/edit", views.editTask, name="editTask"),
    path("add/", views.addTask, name="addTask"),
]
