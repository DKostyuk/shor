from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)


class ServiceOrderForm(forms.ModelForm):

    class Meta:
        model = ServiceOrder
        fields = ["session_key", "status", "customer_name", "customer_phone", "customer_email",
                  "customer_city", "comments"]
