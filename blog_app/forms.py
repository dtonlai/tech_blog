from django import forms
from django.contrib.auth.models import User
from blog_app.models import models

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
