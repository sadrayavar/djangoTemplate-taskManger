from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url="/account/login/")
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("taskList")
    else:
        form = TaskForm()

    return render(request, "taskForm.html", {"form": form})


@login_required(login_url="/accounts/login/")
def taskList(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, "taskList.html", {"tasks": tasks})


@login_required(login_url="/accounts/login/")
def singleTask(request, taskId):
    taskDetail = Task.objects.get(id=taskId)
    return render(request, "singleTask.html", {"task": taskDetail})
