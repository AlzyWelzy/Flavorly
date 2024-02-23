from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfileModel


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
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
        model = User
        fields = ["first_name", "last_name", "email"]
