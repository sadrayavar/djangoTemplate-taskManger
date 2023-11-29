from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from taskManager.constant import tabs, profileTitles, logo


# Create your views here.
def account(request):
    header = {"tabs": tabs, "title": profileTitles["profile"], "logo": logo}

    return render(request, "account.html", {**header})


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("explorePage")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("explorePage")
    else:
        form = UserCreationForm()
        header = {"tabs": tabs, "title": profileTitles["register"], "logo": logo}
        return render(request, "register.html", {"form": form, **header})
