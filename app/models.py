from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_picture", blank=True, null=True
    )

    def get_full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.username
