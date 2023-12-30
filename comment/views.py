from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from task.models import Task
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from taskManager.constant import logo, commentTitles, dynamicTabs


# Create your views here.
def addComment(request, taskId):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user if request.user.is_authenticated else None
            comment.task = Task.objects.get(id=taskId)
            comment.save()

            return redirect("..")
    else:
        form = CommentForm()

    header = {
        "tabs": dynamicTabs("", request.user),
        "logo": logo,
        "title": commentTitles["add"],
    }
    data = {"form": form, "edit": False}
    return render(request, "commentForm.html", {**data, **header})


@login_required
def deleteComment(request, taskId, commentId):
    comment = Comment.objects.get(id=commentId)
    if comment.user == request.user:
        comment.delete()
        return redirect(reverse("taskPage", args=[taskId]))
    else:
        return HttpResponseForbidden()


@login_required
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
        comments = Comment.objects.filter(task=taskId)
        header = {
            "tabs": dynamicTabs("", request.user),
            "logo": logo,
            "title": f"{commentTitles['edit']} {comment.text[0:10]}...",
        }
        data = {
            "form": CommentForm(instance=comment),
            "edit": True,
            "task": Task.objects.get(id=taskId),
            "comments": comments,
            "commentsCount": len(comments),
        }

        return render(request, "taskPage.html", {**data, **header})


@login_required
def myComments(request):
    comments = Comment.objects.filter(user=request.user)

    header = {
        "tabs": dynamicTabs("myCommentsPage", request.user),
        "logo": logo,
        "title": commentTitles["my"],
    }
    data = {"comments": comments, "commentsCount": len(comments), "my": True}

    return render(request, "myComments.html", {**header, **data})
