"""Student forms"""
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from student.models import Student


class SignupForm(forms.Form):
    """Sign up Form"""
    password = forms.CharField(
        min_length=3,
        max_length=70,
        widget=forms.PasswordInput()
    )

    password_confirmation = forms.CharField(
        min_length=3,
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    phone_number = forms.CharField(min_length=11, max_length=13)

    def clean(self):
        """Verified password and password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseña no son iguales')

        return data

    def save(self):
        """Create a new student"""

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        student = Student(user=user, phone_number=data['phone_number'])
        student.save()
