from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    address = forms.CharField(label="Address")
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "address", "password1", "password2"]