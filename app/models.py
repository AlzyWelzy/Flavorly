from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfileModel(AbstractUser):
    email = models.EmailField(blank=True, null=True, unique=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture", blank=True, null=True
    )

    def get_full_name(self):
        return super().get_full_name()

    def __str__(self):
        return self.username
