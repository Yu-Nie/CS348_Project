from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Restaurant, Food
from .utils import getRestrantsOwner


class SignupForm(UserCreationForm):
    username = forms.EmailField(label="Email")
    email = forms.EmailField(widget=forms.HiddenInput())
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    address = forms.CharField(label="Address")
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "address", "password1", "password2", "email"]


class AddRestaurantForm(forms.ModelForm):
    name = forms.CharField(label="Restaurant Name")
    address = forms.CharField(label="Adress")
    image_url = forms.CharField(label="Image URL")
    phone = forms.IntegerField(label="Phone Number")
    class Meta:
        model = Restaurant
        fields = ["name", "address", "image_url", "phone"]


class AddFoodForm(forms.ModelForm):
    name = forms.CharField(label="Food Name")
    description = forms.CharField(label="Description")
    price = forms.FloatField(label="Price")
    image_url = forms.CharField(label="Image URL")

    class Meta:
        model = Food
        fields = ["name", "description", "price", "image_url"]
