from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from task.models import Task
from taskManager.constant import generateBasicData, logo, taskTitles, dynamicTabs
from comment.models import Comment


def adminHomePage(request):
    if request.user.is_superuser:
        comments = Comment.objects.all()
        tasks = Task.objects.filter(approved=False)

        data = {
            "adminConsole": True,
            "comments": comments,
            "commentsCount": len(comments),
            "tasks": tasks,
            "tasksCount": len(tasks),
        }
        context = generateBasicData(request, "adminPage", "admin")
        return render(request, "adminPage.html", {**context, **data})
    else:
        return HttpResponseForbidden()


def hideComment(request, commentId):
    if request.user.is_superuser:
        comment = Comment.objects.get(id=commentId)
        comment.hidden = True if comment.hidden == False else False
        comment.save()
        return redirect("adminPage")
    else:
        return HttpResponseForbidden()


def approveTask(request, taskId):
    if request.user.is_superuser:
        task = Task.objects.get(id=taskId)
        task.approved = True if task.approved == False else False
        task.save()
        return redirect("adminPage")
    else:
        return HttpResponseForbidden()
