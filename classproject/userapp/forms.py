from classproject.store.models import Profile
from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#######################

class customerform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [

            'address',
            'profile_picture',
            'identification',
            'nationality',
        ]