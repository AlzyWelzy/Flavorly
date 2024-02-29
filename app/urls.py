from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my_account/", views.my_account, name="my_account"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("recipe-detail/<slug:slug>", views.recipe_detail, name="recipe_detail"),
    path("post-recipe/", views.post_recipe, name="post_recipe"),
    path("update-recipe/<slug:slug>", views.update_recipe, name="update_recipe"),
    path("delete-recipe/<slug:slug>", views.delete_recipe, name="delete_recipe"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("add-profile-picture/", views.add_profile_picture, name="add_profile_picture"),
    path("register/", views.register, name="register"),
    path("verify-otp", views.is_verified, name="verify_otp"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_details, name="post_details"),
]
