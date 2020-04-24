from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(),
    username = forms.CharField(max_length=10, help_text="Id number without '-' symbol.", label='ID Number')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']