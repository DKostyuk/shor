from django import forms
from .models import *


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["receiver_name", "receiver_surname", "receiver_father_name", "receiver_email",
                  "receiver_phone", "receiver_delivery_address"]


class ServiceOrderForm(forms.ModelForm):

    class Meta:
        model = ServiceOrder
        fields = ["session_key", "status", "customer_name", "customer_phone", "customer_email",
                  "customer_city", "comments"]
