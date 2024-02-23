from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserProfileForm, AddProfilePictureForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserProfileModel

from django.contrib.auth.models import auth


# Create your views here.


@login_required(login_url="login")
def index(request):

    return render(request, "app/index.html")


def dashboard_view(request):
    return render(request, "app/dashboard.html")


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()

            UserProfileModel.objects.create(
                user=user,
            )

            login(response, user)

            return redirect("index")

    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


@login_required(login_url="login")
def edit_profile(request):
    user_profile = request.user

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("edit_profile")  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "app/edit_profile.html", {"form": form})


@login_required(login_url="login")
def add_profile_picture(request):
    if request.method == "POST":
        form = AddProfilePictureForm(
            request.POST, request.FILES, instance=request.user.userprofilemodel
        )
        if form.is_valid():
            form.save()
            return redirect("edit_profile")  # Redirect to the user's profile page
    else:
        form = AddProfilePictureForm(instance=request.user.userprofilemodel)

    return render(request, "app/edit_profile.html", {"form": form})


"""
Template for login (temporary)
Not used anymore
"""
# def my_login(request):
#     form = LoginForm()

#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)

#         if form.is_valid():
#             username = request.POST.get("username")
#             password = request.POST.get("password")

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect("index")
#             else:
#                 messages.info(request, "Username or Password is incorrect")
#     context = {"form": form}

#     return render(request, "app/signin.html", context)
