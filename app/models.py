from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import generate_slug

# Create your models here.


class UserProfileModel(AbstractUser):

    email = models.EmailField(blank=True, null=True, unique=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture", blank=True, null=True
    )

    otp = models.IntegerField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)

    def get_full_name(self):
        return super().get_full_name()

    def __str__(self):
        return self.username


class RecipeModel(models.Model):
    author = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to="food_picture/", blank=False, null=False, default=""
    )
    ingredients = models.TextField(blank=False, null=False, default="")
    instructions = models.TextField(blank=False, null=False, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)
