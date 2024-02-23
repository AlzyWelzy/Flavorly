from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserProfileModel

# Create your views here.


@login_required(login_url="login")
def index(request):
    return render(request, "app/index.html")


def signin_view(request):

    return render(request, "app/signin.html")


def dashboard_view(request):
    return render(request, "app/dashboard.html")


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()

            login(response, user)
            print(user)

            UserProfileModel.objects.create(user=user)

            messages.success(response, "Registration Successful!")
            return redirect("index")

    else:
        form = RegisterForm()

    return render(response, "app/register.html", {"form": form})
