from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TaskForm
from .models import Task

tabs = [
    {"text": "Add", "link": "addTask", "class": "link-primary"},
    {"text": "Home", "link": "allTasks", "class": ""},
    {"text": "Exlplore", "link": "userTasks", "class": ""},
]


@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("allTasks")
    else:
        form = TaskForm()

    context = {"form": form, "tabs": tabs, "title": "Add Task"}
    return render(request, "taskForm.html", context)


@login_required
def userTasks(request):
    tasks = Task.objects.filter(user=request.user)

    context = {"tasks": tasks, "count": len(tasks), "tabs": tabs, "title": "My Tasks"}
    return render(request, "taskList.html", context)


@login_required
def allTasks(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
        "count": len(tasks),
        "tabs": tabs,
        "title": "People Tasks",
    }
    return render(request, "taskList.html", context)


@login_required
def singleTask(request, taskId):
    task = Task.objects.get(id=taskId)

    context = {
        "task": task,
        "owner": request.user == task.user,
        "tabs": tabs,
        "title": f"Task {task.title}",
    }
    return render(request, "singleTask.html", context)


@login_required
def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)  # .delete()

    if task.user == request.user:
        task.delete()
        return redirect("allTasks")

    else:
        return HttpResponseForbidden()


@login_required
def editTask(request, taskId):
    task = Task.objects.get(id=taskId)
    if request.method == "POST":
        if task.user == request.user:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                print(task.title)
                task.save()
                print(task.title)
                return redirect(".")
        else:
            return HttpResponseForbidden()
    else:
        form = TaskForm(instance=task)
        context = {
            "tabs": tabs,
            "form": form,
            "title": f"Edit {task.title}",
        }
        return render(request, "taskForm.html", context)
