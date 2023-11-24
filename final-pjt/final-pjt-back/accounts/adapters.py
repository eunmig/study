from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field
from allauth.utils import get_username_max_length
from allauth.account import app_settings as allauth_settings
from .models import User

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        """
        Saves a new `User` instance using information provided in the
        registration form.
        """
        user = super().save_user(request, user, form, commit)
        user.salary = form.cleaned_data.get('salary')
        user.save()
        return user