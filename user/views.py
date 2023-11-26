from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("taskList")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
