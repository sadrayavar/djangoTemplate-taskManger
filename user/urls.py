from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerUser),
    path("edit/", views.editUser),
    path("delete/", views.deleteUser),
]
