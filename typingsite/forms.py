from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(required = True)
    lastname = forms.CharField(required = True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email", "password1", "password2"]