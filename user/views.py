from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from taskManager.constant import profileTitles, generateBasicData
from .models import User
from .forms import UserRegistratoinForm, UserLoginForm, UserEditionForm
from task.signals import getTaskCount


# Create your views here.
@login_required
def editUser(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UserEditionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profilePage")
    else:
        form = UserEditionForm(instance=request.user)

    data = {"form": form, "editUser": True}
    context = generateBasicData(
        request, "profilePage", f"{profileTitles['profile']} {user.username}"
    )
    return render(request, "profile.html", {**context, **data})


@login_required
def deleteUser(request):
    user = User.objects.get(id=request.user.id)
    user.is_active = False
    user.save()

    return redirect("homePage")


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("homePage")

    if request.method == "POST":
        form = UserRegistratoinForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homePage")

    else:
        form = UserRegistratoinForm()

    data = {"form": form}
    context = generateBasicData(request, "profilePage", "register")
    return render(request, "profile.html", {**context, **data})


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("homePage")

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homePage")
    else:
        form = UserLoginForm()

    data = {"form": form}
    context = generateBasicData(request, "profilePage", "login")
    return render(request, "login.html", {**context, **data})


def logoutUser(request):
    logout(request)
    return redirect("homePage")
