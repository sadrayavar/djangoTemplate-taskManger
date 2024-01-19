from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from taskManager.constant import taskTitles, generateBasicData
from .forms import TaskForm
from .models import Task
from comment.forms import CommentForm
from comment.models import Comment
from .signals import getTaskCount


@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.approved = request.user.is_superuser
            task.save()
            return redirect("homePage")
    else:
        form = TaskForm()

    data = {"form": form}
    context = generateBasicData(request, "addTaskPage", "add")
    return render(request, "taskForm.html", {**context, **data})


@login_required
def myTasks(request):
    tasks = Task.objects.filter(user=request.user)

    data = {"tasks": tasks, "tasksCount": len(tasks)}
    context = generateBasicData(request, "myTasksPage", "myTasks")
    return render(request, "home.html", {**context, **data})


def home(request):
    tasks = Task.objects.all()

    data = {"tasks": tasks, "tasksCount": len(tasks)}
    context = generateBasicData(request, "homePage", "home")
    return render(request, "home.html", {**context, **data})


def task(request, taskId):
    task = Task.objects.get(id=taskId)
    comments = Comment.objects.filter(task=taskId, hidden=False)

    data = {
        "form": CommentForm(),
        "task": task,
        "comments": comments,
        "commentsCount": len(comments),
    }
    context = generateBasicData(
        request, "taskPage", f"{taskTitles['task']} {task.title}"
    )
    return render(request, "taskPage.html", {**context, **data})


@login_required
def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)

    if not task.approved:
        return HttpResponseForbidden()

    if task.user == request.user:
        task.delete()
        return redirect("homePage")

    else:
        return HttpResponseForbidden()


@login_required
def editTask(request, taskId):
    task = Task.objects.get(id=taskId)

    if task.approved:
        if request.method == "POST":
            if task.user == request.user:
                form = TaskForm(request.POST, request.FILES, instance=task)
                if form.is_valid():
                    task.save()
                    return redirect(".")
            else:
                return HttpResponseForbidden()
        else:
            data = {"form": TaskForm(instance=task)}
            context = generateBasicData(
                request, "editTaskPage", f"{taskTitles['edit']} {task.title}"
            )
            return render(request, "taskForm.html", {**data, **context})
    else:
        return HttpResponseForbidden()
