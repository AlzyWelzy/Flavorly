from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileModel, FoodModel


class RegisterForm(UserCreationForm):

    class Meta:
        model = UserProfileModel
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class AddProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ["profile_picture"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ["first_name", "last_name", "email"]


class PostForm(forms.ModelForm):
    class Meta:
        model = FoodModel
        fields = ["title", "description", "picture"]
