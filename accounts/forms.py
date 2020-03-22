from django import forms
from .views import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True,
                            widget=forms.EmailInput(), help_text='example@gmail.com')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
