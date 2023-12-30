from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from taskManager.constant import tabs, profileTitles, logo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserChangeForm
from .models import User
from .forms import UserRegistratoinForm, UserLoginForm, UserEditoinForm
from taskManager.constant import profileTitles, logo, dynamicTabs


# Create your views here.
@login_required
def editUser(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UserEditoinForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profilePage")
    else:
        form = UserEditoinForm(instance=request.user)

    header = {
        "tabs": dynamicTabs("profilePage"),
        "logo": logo,
        "title": f"{profileTitles['profile']} {user.username}",
    }
    data = {"form": form, "edit": True}

    return render(request, "userForm.html", {**data, **header})


@login_required
def deleteUser(request):
    User.objects.get(id=request.user.id).is_active = False
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

    header = {
        "tabs": dynamicTabs("profilePage"),
        "title": profileTitles["register"],
        "logo": logo,
    }
    return render(request, "userForm.html", {"form": form, **header})


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

    context = {
        "tabs": dynamicTabs("profilePage"),
        "title": profileTitles["login"],
        "logo": logo,
    }
    return render(request, "login.html", {"form": form, **context})
