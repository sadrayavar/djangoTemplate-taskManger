from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from task.models import Task
from .models import Comment
from .forms import CommentForm
from taskManager.constant import tabs, logo, commentTitles


# Create your views here.
def addComment(request, taskId):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.task = Task.objects.get(id=taskId)
            comment.save()

            return redirect("..")
    else:
        header = {"tabs": tabs, "logo": logo, "title": commentTitles["add"]}
        data = {"form": CommentForm(), "edit": False}

        return render(request, "commentForm.html", {**data, **header})


def deleteComment(request, taskId, commentId):
    comment = Comment.objects.get(id=commentId)
    if comment.user == request.user:
        comment.delete()
        return redirect(reverse("taskPage", args=[taskId]))
    else:
        return HttpResponseForbidden()


def editComment(request, taskId, commentId):
    comment = Comment.objects.get(id=commentId)
    if request.method == "POST":
        if comment.user == request.user:
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment.save()
                return redirect("../..")
        else:
            return HttpResponseForbidden()
    else:
        header = {
            "tabs": tabs,
            "logo": logo,
            "title": f"{commentTitles['edit']} {comment.text[0:10]}...",
        }
        data = {"form": CommentForm(instance=comment), "edit": True}

        return render(request, "commentForm.html", {**data, **header})
