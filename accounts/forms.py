from django import forms
from .models import *
from django.forms import ModelForm

class AddContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['name','mobile']
