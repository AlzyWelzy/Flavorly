from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserProfileForm, AddProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserProfileModel
from .models import UserProfileModel

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
                full_name=form.cleaned_data["full_name"],
                email=form.cleaned_data["email"],
            )

            login(response, user)

            return redirect("index")

    else:
        form = RegisterForm()

    return render(response, "app/register.html", {"form": form})


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
