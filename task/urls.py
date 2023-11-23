from django.urls import path, include
from . import views

urlpatterns = [
    path("add/", views.addTask),
    path("edit/", views.editTask),
    path("delete/", views.deleteTask),
]
