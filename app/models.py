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
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    food_type = models.CharField(max_length=100)
    food_picture = models.ImageField(upload_to="food_picture", blank=True, null=True)

    def __str__(self):
        return self.food_name
