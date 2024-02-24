from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my_account/", views.my_account, name="my_account"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("recipe_detail/<int:pk>", views.recipe_detail, name="recipe_detail"),
    path("post_recipe/", views.post_recipe, name="post_recipe"),
    path("update_recipe/<int:pk>", views.update_recipe, name="update_recipe"),
    path("delete_recipe/<int:pk>", views.delete_recipe, name="delete_recipe"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("add_profile_picture/", views.add_profile_picture, name="add_profile_picture"),
    path("register/", views.register, name="register"),
]
