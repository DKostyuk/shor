from django import forms
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TestEditorForm(forms.ModelForm):

    class Meta:
        model = TestEditor
        fields = ["comments"]


class CalendarTrainingForm(forms.ModelForm):

    class Meta:
        model = CalendarTraining
        fields = ["calendar_name", "date_picked_from", "date_picked_until", "comments"]
        widgets = {
            'date_picked_from': DatePickerInput(),  # default date-format %m/%d/%Y will be used
            'date_picked_until': DatePickerInput(format='%Y-%m-%d'),  # specify date-format
        }

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#
# class LetterForm(forms.ModelForm):
#
#     class Meta:
#         model = Letter
#         fields = ["subject", "from_name", "email_sender", "city_sender", "message"]
#
#
# class TrainingUserForm(forms.ModelForm):
#
#     class Meta:
#         model = TrainingUser
#         fields = ["trainee_name", "trainee_email", "trainee_tel_number", "training", "comments"]


class ProductFileCSVForm(forms.ModelForm):

    class Meta:
        model = ProductFileCSV
        fields = ["file_name", "document", "is_active", "comments"]
