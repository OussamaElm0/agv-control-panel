from django import forms
from .models import *

class AdminLoginForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ['username', 'password']