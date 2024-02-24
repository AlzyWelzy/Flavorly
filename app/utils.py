from django.contrib import messages


def activateEmail(request, user, to_email):
    messages.success(
        request,
        f"Account successfully created for {user}. An email has been sent to {to_email} with instructions to activate the account. Please check your spam folder. The link will expire in 15 minutes.",
    )
