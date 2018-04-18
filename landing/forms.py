from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ["tel_number", "nip", "company_name", "index", "city", "street", "locality"]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = ["subject", "from_name", "email_sender", "city_sender", "message"]
