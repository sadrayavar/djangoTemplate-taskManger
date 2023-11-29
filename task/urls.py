from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.explore, name="explorePage"),
    path("myTasks/", views.home, name="homePage"),
    path("<int:taskId>/", views.task, name="taskPage"),
    path("<int:taskId>/delete", views.deleteTask, name="deleteTaskPage"),
    path("<int:taskId>/edit", views.editTask, name="editTaskPage"),  # type: ignore
    path("add/", views.addTask, name="addTaskPage"),
]
