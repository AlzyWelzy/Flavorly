from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]
