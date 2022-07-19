from django import forms
from django.db.models.enums import Choices
# from django.forms.fields import forms
from classproject.paymentapp.models import Order_table

class AddToCart_form(forms.ModelForm):
    class Meta:
        model = Order_table
        fields = [
            'quantity'
        ]
    # quantity = forms.CharField(max_length=30, required=True)

class paymentOption_form(forms.Form):
    Choices = [ ('masterCard', ''),
                ('visaCard', ''),
                ('payOnDelivery', ''),
                ]
    option = forms.ChoiceField(choices= Choices, widget=forms.RadioSelect, label="")

class CardDetails_form(forms.Form):
    card_name = forms.CharField(max_length=20, help_text='Enter Card Name', label='')
    card_number = forms.CharField(max_length=16, help_text='Enter Card Number', label='')
    card_cvv = forms.CharField(max_length=3, help_text='Enter CVV', label='')
    card_expiry_date = forms.CharField(max_length=5, help_text='Enter Card Expiry date (MM/YY)', label='')
    