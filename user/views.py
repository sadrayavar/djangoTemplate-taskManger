from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from taskManager.constant import tabs, profileTitles, logo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, User
from .forms import UserRegistratoinForm, UserLoginForm
from taskManager.constant import tabs, profileTitles, logo


# Create your views here.
def account(request):
    header = {"tabs": tabs, "title": profileTitles["profile"], "logo": logo}
    return render(request, "account.html", {**header})


@login_required
def editUser(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profilePage")
        else:
            return HttpResponseForbidden()
    else:
        form = UserChangeForm(instance=request.user)

    header = {
        "tabs": tabs,
        "logo": logo,
        "title": f"{profileTitles['profile']} {user.username}",
    }
    data = {"form": form}

    return render(request, "register.html", {**data, **header})


@login_required  # type: ignore
def deleteUser(request):
    User.objects.get(id=request.user.id).is_active = False
    redirect("homePage")


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("homePage")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homePage")

    else:
        form = UserCreationForm()

    header = {"tabs": tabs, "title": profileTitles["register"], "logo": logo}
    return render(request, "register.html", {"form": form, **header})


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
                print("###########", user)
                login(request, user)
                # Redirect to success page or home page
                return redirect("homePage")
    else:
        form = UserLoginForm()

    context = {"tabs": tabs, "title": profileTitles["login"], "logo": logo}
    return render(request, "login.html", {"form": form, **context})
