from classproject.store.models import Product_table, Profile
from classproject.store.models import staff_table
from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#  old form 
# class Product_form(forms.Form):
#     Product_name = forms.CharField(max_length=250)
#     Price = forms.CharField(max_length=250)
#     Quantity = forms.CharField(max_length=250)
#     Description = forms.CharField(widget=forms.Textarea())
#     picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), max_length=5000)
    

class Product_form(forms.ModelForm):
    class Meta:
        model = Product_table
        fields = [
            'product_name',
            'price',
            'quantity',
            'description',
            'profile_picture',
        ]
        
        widgets = {
            'description': forms.Textarea(attrs={'cols':100, 'row': 10})
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a Valid Email')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class Userform(forms.ModelForm):
    class Meta:
        model =User
        fields = [

            'first_name',
            'last_name',
            'email',
        ]
        

class Staffform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'status',
            'position',
            'address',
            'profile_picture',
            'identification',
            'nationality',
            'particulars',
            'state',
        ]
        


class customerform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [

            'address',
            'profile_picture',
            'identification',
            'nationality',
        ]