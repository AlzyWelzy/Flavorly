from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def index(request):
    return render(request, "app/index.html")


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = RegisterForm()

    return render(response, "app/register.html", {"form": form})
