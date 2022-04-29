import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.EmailField(label="Email")
    email = forms.EmailField(widget=forms.HiddenInput())
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    address = forms.CharField(label="Address")
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "address", "password1", "password2", "email"]