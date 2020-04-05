# Ebiun forms

# Django
from django import forms


class ContactForm(forms.Form):
    """Contact form"""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class LoginForm(forms.Form):
    """Login form"""

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    password = forms.CharField(
        min_length=3,
        max_length=70,
        widget=forms.PasswordInput()
    )


