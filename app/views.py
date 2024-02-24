from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfileForm, AddProfilePictureForm, PostForm
from verify_email.email_handler import send_verification_email
from .utils import activateEmail


def index(request):
    return render(request, "app/index.html")


@login_required(login_url="login")
def dashboard(request):

    return render(request, "app/dashboard.html")


@login_required(login_url="login")
def my_account(request):
    user = request.user
    return render(request, "app/my_account.html")


def register(request):

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            activateEmail(request, inactive_user, form.cleaned_data.get("email"))
            # user = form.save()

            # user.save()

            # UserProfileModel.objects.create(
            #     user=user,
            # )

            # login(request, user)

            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required(login_url="login")
def edit_profile(request):
    user_profile = request.user

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "app/edit_profile.html", {"form": form})


@login_required(login_url="login")
def add_profile_picture(request):
    if request.method == "POST":
        form = AddProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")  # Redirect to the user's profile page
    else:
        # form = AddProfilePictureForm(instance=request.user.userprofilemodel)
        form = AddProfilePictureForm()

    return render(request, "app/edit_profile.html", {"form": form})
