from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import TaskForm
from .models import Task

# navList = [
#     {"label": "Discover", "url": "taskList"},
#     {"label": "Home", "url": "userTasks"},
#     {"label": "Profile", "url": "account"},
# ]


@login_required(login_url="loginUser")
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

    return render(request, "taskForm.html", {"form": form})


@login_required(login_url="loginUser")
def userTasks(request):
    tasks = Task.objects.filter(user=request.user)

    context = {"tasks": tasks, "count": len(tasks)}
    return render(request, "taskList.html", context)


@login_required(login_url="loginUser")
def allTasks(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks, "count": len(tasks)}
    return render(request, "taskList.html",context)


@login_required(login_url="loginUser")
def singleTask(request, taskId):
    task = Task.objects.get(id=taskId)

    context = {"task": task, "owner": request.user == task.user}
    return render(request, "singleTask.html", context)


@login_required(login_url="loginUser")
def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)  # .delete()

    if task.user == request.user:
        task.delete()
        messages.success(
            request,
            f"To do with id of {taskId} is deleted succesfully.",
            extra_tags="success",
        )
        return redirect("allTasks")

    else:
        return HttpResponseForbidden()


@login_required(login_url="loginUser")
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
        return render(request, "taskForm.html", {"form": form})
