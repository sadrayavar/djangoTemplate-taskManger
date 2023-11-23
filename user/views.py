from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def registerUser(request):
    return HttpResponse("register user page")


def loginUser(request):
    return render(request, "login.html")


def editUser(request):
    return HttpResponse("edit user page")


def deleteUser(request):
    return HttpResponse("delete user page")
