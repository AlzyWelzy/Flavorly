from django.contrib import messages
from django.utils.text import slugify
import uuid


def activateEmail(request, user, to_email):
    messages.success(
        request,
        f"Account successfully created for {user}. An email has been sent to {to_email} with instructions to activate the account. Please check your spam folder. The link will expire in 15 minutes.",
    )


def generate_slug(title):
    from app.models import RecipeModel

    slug = slugify(title)
    unique_slug = slug
    num = 1
    while RecipeModel.objects.filter(slug=unique_slug).exists():
        # unique_slug = f"{slug}-{num}"
        unique_slug = f"{slug}-{str(uuid.uuid4())[:8]}"
        num += 1
    return unique_slug
