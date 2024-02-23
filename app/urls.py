from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard_view, name="dashboard_view"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("signin/", views.signin_view, name="signin_view"),
    path("add_profile_picture/", views.add_profile_picture, name="add_profile_picture"),
    path("register/", views.register, name="register"),
]
