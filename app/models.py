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


class FoodModel(models.Model):
    author = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="food_picture", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
