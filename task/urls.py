from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.taskList, name="taskList"),
    path("<int:taskId>/", views.singleTask, name="singleTask"),
    path("add/", views.addTask),
]
