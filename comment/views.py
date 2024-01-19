from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from task.models import Task
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from taskManager.constant import generateBasicData, commentTitles


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

    data = {"form": form, "editComment": False}
    context = generateBasicData(request, "", "add")
    return render(request, "commentForm.html", {**context, **data})


@login_required
def deleteComment(request, taskId, commentId):
    comment = Comment.objects.get(id=commentId)
    if comment.user == request.user:
        comment.delete()
        referer = request.META.get("HTTP_REFERER")[-9:-1]
        if referer == "comments":
            return redirect("myCommentsPage")
        else:
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

        data = {
            "form": CommentForm(instance=comment),
            "editComment": True,
            "task": Task.objects.get(id=taskId),
            "comments": comments,
            "commentsCount": len(comments),
        }
        context = generateBasicData(
            request, "", f"{commentTitles['edit']} {comment.text[0:10]}..."
        )
        return render(request, "taskPage.html", {**context, **data})


@login_required
def myComments(request):
    comments = Comment.objects.filter(user=request.user)

    data = {"comments": comments, "commentsCount": len(comments)}
    context = generateBasicData(request, "myCommentsPage", "my")
    return render(request, "myComments.html", {**context, **data})
