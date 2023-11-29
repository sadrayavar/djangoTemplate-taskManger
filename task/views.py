from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from taskManager.constant import tabs, logo, taskTitles
from .forms import TaskForm
from .models import Task
from comment.forms import CommentForm
from comment.models import Comment
from comment.views import addComment


@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("homePage")
    else:
        form = TaskForm()

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["add"]}
    data = {"form": form}

    return render(request, "taskForm.html", {**data, **header})


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["home"]}
    data = {"tasks": tasks, "count": len(tasks)}

    return render(request, "taskList.html", {**data, **header})


@login_required
def explore(request):
    tasks = Task.objects.all()

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["explore"]}
    data = {"tasks": tasks, "count": len(tasks)}

    return render(request, "taskList.html", {**data, **header})


@login_required
def task(request, taskId):
    task = Task.objects.get(id=taskId)
    comments = Comment.objects.filter(task=taskId)

    header = {
        "tabs": tabs,
        "logo": logo,
        "title": f"{taskTitles['task']} {task.title}",
    }
    data = {"task": task, "comments": comments, "user": request.user}
    commentForm = {"form": CommentForm()}

    return render(request, "singleTask.html", {**header, **data, **commentForm})


@login_required
def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)
    if task.user == request.user:
        task.delete()
        return redirect("homePage")

    else:
        return HttpResponseForbidden()


@login_required
def editTask(request, taskId):
    task = Task.objects.get(id=taskId)
    if request.method == "POST":
        if task.user == request.user:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                task.save()
                return redirect(".")
        else:
            return HttpResponseForbidden()
    else:
        header = {
            "tabs": tabs,
            "logo": logo,
            "title": f"{taskTitles['edit']} {task.title}",
        }
        data = {"form": TaskForm(instance=task)}

        return render(request, "taskForm.html", {**data, **header})
