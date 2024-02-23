from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard_view, name="dashboard_view"),
    path("signin/", views.signin_view, name="signin_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("register/", views.register, name="register"),
]
