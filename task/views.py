from django.shortcuts import render


# Create your views here.
def addTask(request):
    return render(request, "addTask.html")


def editTask(request):
    return render(request, "editTask.html")


def deleteTask(request):
    return render(request, "deleteTask.html")
