from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def user(request):
    return HttpResponse("edit user page")


def registerUser(request):
    return HttpResponse(
        "register user page"
    )  # TODO Zahra : create a template for register like i did for loginUser below


def loginUser(request):
    return render(request, "login.html")
