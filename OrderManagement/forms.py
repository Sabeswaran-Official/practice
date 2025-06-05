from django import forms
from .models import *

class Customer_Form(forms.ModelForm):

    class Meta:

        model = Customer
        fields = '__all__'

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'customer_since': forms.DateInput(attrs={'class': 'form-control backclass'}),
        }

class Orders_Form(forms.ModelForm):

    class Meta:

        model = Orders
        fields = ['customer_reference', 'product_reference', 'order_number', 'order_date', 'quantity']

        widgets = {
            'customer_reference': forms.Select(attrs={'class': 'form-control backclass'}),
            'product_reference': forms.Select(attrs={'class': 'form-control backclass'}),
            'order_number': forms.TextInput(attrs={'class': 'form-control backclass'}),
            'order_date': forms.DateInput(attrs={'class': 'form-control backclass'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control backclass'}),
        }