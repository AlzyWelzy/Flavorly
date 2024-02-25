from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email
from .utils import activateEmail
from .forms import RegisterForm, UserProfileForm, AddProfilePictureForm, RecipeForm
from .models import RecipeModel


def index(request):
    recipes = RecipeModel.objects.all()
    context = {"recipes": recipes}
    return render(request, "app/index.html", context)


def recipe_detail(request, pk):
    recipe = RecipeModel.objects.get(id=pk)
    context = {"recipe": recipe}
    return render(request, "app/recipe_detail.html", context)


@login_required
def dashboard(request):
    recipes = RecipeModel.objects.filter(author=request.user)

    context = {"recipes": recipes}

    return render(request, "app/dashboard.html", context)


@login_required
def post_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            food_post = form.save(commit=False)
            food_post.author = user
            food_post.save()
            return redirect("dashboard")
        else:
            form = RecipeForm()

    else:
        form = RecipeForm()

    context = {"form": form}

    return render(request, "app/create_post.html", context)


@login_required
def update_recipe(request, pk):
    try:
        recipe = get_object_or_404(RecipeModel, id=pk)
    except RecipeModel.DoesNotExist:
        messages.info(request, "Recipe does not exist.")
        return redirect("dashboard")

    if recipe.author != request.user:
        messages.info(request, "You can only edit your own recipes.")
        return redirect("dashboard")

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, "app/create_post.html", {"form": form})


@login_required
def delete_recipe(request, pk):
    try:
        recipe = get_object_or_404(RecipeModel, id=pk)
    except RecipeModel.DoesNotExist:
        messages.info(request, "Recipe does not exist.")
        return redirect("dashboard")

    if recipe.author == request.user:
        recipe.delete()
    else:
        messages.info(request, "You can only delete your own recipes.")
    return redirect("dashboard")


@login_required
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


@login_required
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


@login_required
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
