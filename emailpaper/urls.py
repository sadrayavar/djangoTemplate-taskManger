from django.urls import path
from . import views

urlpatterns = [
    path("", views.newspaper, name="newspaperPage"),
]
