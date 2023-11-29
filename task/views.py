from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TaskForm
from .models import Task
from taskManager.constant import tabs, logo, taskTitles


@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("explorePage")
    else:
        form = TaskForm()

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["add"]}
    context = {"form": form}
    context.update(header)

    return render(request, "taskForm.html", context)


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["home"]}
    context = {"tasks": tasks, "count": len(tasks)}
    context.update(header)

    return render(request, "taskList.html", context)


@login_required
def explore(request):
    tasks = Task.objects.all()

    header = {"tabs": tabs, "logo": logo, "title": taskTitles["explore"]}
    context = {"tasks": tasks, "count": len(tasks)}
    context.update(header)

    return render(request, "taskList.html", context)


@login_required
def task(request, taskId):
    task = Task.objects.get(id=taskId)

    header = {"tabs": tabs, "logo": logo, "title": f"{taskTitles['task']} {task.title}"}
    context = {"task": task, "owner": request.user == task.user}
    context.update(header)

    return render(request, "singleTask.html", context)


@login_required
def deleteTask(request, taskId):
    task = Task.objects.get(id=taskId)  # .delete()

    if task.user == request.user:
        task.delete()
        return redirect("explorePage")

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
        header = {
            "tabs": tabs,
            "logo": logo,
            "title": f"{taskTitles['edit']} {task.title}",
        }
        context = {"form": TaskForm(instance=task)}
        context.update(header)

        return render(request, "taskForm.html", context)
