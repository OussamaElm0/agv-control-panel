from django import forms
from django.contrib.auth.models import User

class AdminLoginForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100, error_messages={'required': 'Please enter a username.'})
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, error_messages={'required': 'Please enter a password.'})

    class Meta:
        model = User
        fields = ['username', 'password']