from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from taskManager.constant import tabs, profileTitles, logo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import CustomUser
from .forms import UserRegistratoinForm


# Create your views here.
def account(request):
    header = {"tabs": tabs, "title": profileTitles["profile"], "logo": logo}
    return render(request, "account.html", {**header})


@login_required
def editUser(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UserRegistratoinForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profilePage")
        else:
            return HttpResponseForbidden()
    else:
        form = UserRegistratoinForm(instance=request.user)

    header = {
        "tabs": tabs,
        "logo": logo,
        "title": f"{profileTitles['profile']} {user.username}",
    }
    data = {"form": form}

    return render(request, "register.html", {**data, **header})


@login_required
def deleteUser(request):
    CustomUser.objects.get(id=request.user.id).is_active = False
    redirect("homePage")


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

    header = {"tabs": tabs, "title": profileTitles["register"], "logo": logo}
    return render(request, "register.html", {"form": form, **header})
