from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from taskManager.constant import tabs, profileTitles, logo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import User


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
            return redirect("logoutUser")
        else:
            return HttpResponseForbidden()
    else:
        header = {
            "tabs": tabs,
            "logo": logo,
            "title": f"{profileTitles['profile']} {user.username}",
        }
        data = {"form": UserChangeForm(instance=request.user)}

        return render(request, "register.html", {**data, **header})

    return


@login_required
def deleteUser(request):
    User.objects.filter(id=request.user.id).delete()
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
