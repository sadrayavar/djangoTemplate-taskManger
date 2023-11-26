from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm
from .models import Task


@login_required(login_url="loginUser")
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("taskList")
    else:
        form = TaskForm()

    return render(request, "taskForm.html", {"form": form})


@login_required(login_url="loginUser")
def taskList(request):
    tasks = Task.objects.all()
    return render(request, "taskList.html", {"tasks": tasks})


@login_required(login_url="loginUser")
def singleTask(request, taskId):
    taskDetail = Task.objects.get(id=taskId)
    return render(request, "singleTask.html", {"task": taskDetail})


@login_required(login_url="loginUser")
def deleteTask(request, taskId):
    Task.objects.get(id=taskId).delete()
    messages.success(
        request,
        f"To do with id of {taskId} is deleted succesfully.",
        extra_tags="success",
    )
    return redirect("taskList")


@login_required(login_url="loginUser")  
def editTask(request, taskId):
    task = Task.objects.get(id=taskId)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task.save()
            return redirect(".")
    else:
        form = TaskForm(instance=task)
        return render(request, "taskForm.html", {"form": form})
