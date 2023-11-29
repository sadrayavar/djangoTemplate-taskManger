from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def account(request):
    return render(request, "account.html")


def registerUser(request):
    if request.user.is_authenticated:
        context = {"mess": "You are already registered."}
        return render(request, "explorePage", context)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("explorePage")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
