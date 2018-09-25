from django import forms
# from django.contrib.auth.models import User
from accounts.models import User
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserAdminCreationForm


class UserRegistrationFrom(UserAdminCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
