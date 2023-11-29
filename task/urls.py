from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.explore, name="homePage"),
    path("myTasks/", views.home, name="myTasksPage"),
    #
    path("<int:taskId>/", include("comment.urls")),
    #
    path("<int:taskId>/", views.task, name="taskPage"),
    path("<int:taskId>/delete", views.deleteTask, name="deleteTaskPage"),
    path("<int:taskId>/edit", views.editTask, name="editTaskPage"),  # type: ignore
    #
    path("add/", views.addTask, name="addTaskPage"),
]
