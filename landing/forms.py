from django import forms
from .models import *
from cosmetologs.models import Cosmetolog, ServiceProduct, ServiceProductImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ["tel_number", "nip", "company_name", "index", "city", "street", "locality"]


class CosmetologForm(forms.ModelForm):

    class Meta:
        model = Cosmetolog
        fields = ["cosmetolog_name", "city", "certificate_image", "cosmetolog_surname",
                  "cosmetolog_father_name", 'tel_number']


class AddServiceForm(forms.ModelForm):

    class Meta:
        model = ServiceProduct
        fields = ["name", "cosmetolog", "price01", "price02", "discount", "description", "short_description",
                  "category", "subcategory"]


class AddServiceImageForm(forms.ModelForm):

    class Meta:
        model = ServiceProductImage
        fields = ["service_product", "image", "is_main", "is_active"]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = ["subject", "from_name", "email_sender", "phone_sender", "city_sender",
                  "message", "cosmetolog_email", "cosmetolog"]


class TrainingUserForm(forms.ModelForm):

    class Meta:
        model = TrainingUser
        fields = ["trainee_name", "trainee_email", "trainee_tel_number", "training", "comments"]
