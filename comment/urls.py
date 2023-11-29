from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.addComment, name="addCommentPage"),
    path("<int:commentId>/delete/", views.deleteComment, name="deleteCommentPage"),
    path("<int:commentId>/edit/", views.editComment, name="editCommentPage"),
]
