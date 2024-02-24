from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserProfileForm, AddProfilePictureForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserProfileModel
from django.contrib.auth.models import auth

...
from verify_email.email_handler import send_verification_email


def activateEmail(request, user, to_email):
    messages.success(
        request,
        f"Your account has been created. We have sent you an email to {to_email}. Please confirm your email to continue.",
    )


def index(request):
    return render(request, "app/index.html")


@login_required(login_url="login")
def dashboard(request):

    return render(request, "app/dashboard.html")


@login_required(login_url="login")
def my_account(request):
    user = request.user
    return render(request, "app/my_account.html")


# Create your views here.
def register(response):

    if response.user.is_authenticated:
        return redirect("dashboard")

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()

            user.save()

            UserProfileModel.objects.create(
                user=user,
            )

            login(response, user)

            return redirect("dashboard")

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
        # form = AddProfilePictureForm(instance=request.user.userprofilemodel)
        form = AddProfilePictureForm()

    return render(request, "app/edit_profile.html", {"form": form})
