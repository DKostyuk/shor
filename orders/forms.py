from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)


class ServiceOrderForm(forms.ModelForm):

    class Meta:
        model = ServiceOrder
        # exclude = [""]
        exclude = ["created", "updated"]
        # exclude = ["total_price", "customer_address", "status", "created", "updated"]
# fields = ["customer_name", "customer_email", "customer_phone", "comments"]
