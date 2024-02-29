from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my_account/", views.my_account, name="my_account"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("recipe_detail/<slug:slug>", views.recipe_detail, name="recipe_detail"),
    path("post_recipe/", views.post_recipe, name="post_recipe"),
    path("update_recipe/<slug:slug>", views.update_recipe, name="update_recipe"),
    path("delete_recipe/<slug:slug>", views.delete_recipe, name="delete_recipe"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("add_profile_picture/", views.add_profile_picture, name="add_profile_picture"),
    path("register/", views.register, name="register"),
    path("verify_otp", views.is_verified, name="verify_otp"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_details, name="post_details"),
]
