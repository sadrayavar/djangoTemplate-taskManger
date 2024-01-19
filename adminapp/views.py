from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from taskManager.constant import logo, taskTitles, dynamicTabs
from comment.models import Comment


def adminHomePage(request):
    if request.user.is_superuser:
        # fmt: off
        header = {"tabs": dynamicTabs("adminPage", request.user),"logo": logo,"title": taskTitles["admin"]}
        data = {"adminConsole":True}

        return render(request, "adminPage.html", {**header, **data, **fetchComments()})
    else:
        return HttpResponseForbidden()


def fetchComments():
    comments = Comment.objects.all()
    return {"comments": comments, "commentsCount": len(comments)}


def hideComment(request, commentId):
    if request.user.is_superuser:
        comment = Comment.objects.get(id=commentId)
        comment.hidden = True if comment.hidden == False else False
        comment.save()
        return redirect("adminPage")
    else:
        return HttpResponseForbidden()
