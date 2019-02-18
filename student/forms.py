"""Student forms"""
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from student.models import Student


class SignupForm(forms.Form):
    """Sign up Form"""

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    phone_number = forms.CharField(min_length=11, max_length=13)

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

    def clean(self):
        """Verified password and password confirmation match"""
        data = super(SignupForm,self).clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseña no son iguales')

        return password

    def clean_email(self):
        """Username must be unique"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(username=email).exists()

        if email_taken:
            raise forms.ValidationError('Email ya esta registrado')
        return email

    # def clean_phone_number(self):
    #     """phone must be between 11 and 13"""
    #     phone = self.cleaned_data['phone_number']
    #
    #     if len((phone)) < 11 or len((phone)) > 13:
    #         raise forms.ValidationError('El celular debe tener 11 digitos minimo y 13 maximo')
    #     return phone

    # def clean_password(self):
    #     data = super().clean()
    #
    #     password = data['password']
    #     password_confirmation = data['password_confirmation']
    #     # password = self.cleaned_data['password']
    #     # password_confirmation = self.cleaned_data['password_confirmation']
    #
    #     if password != password_confirmation:
    #         raise forms.ValidationError('Las contraseña no son iguales')
    #
    #     return password

    def save(self):
        """Create a new student"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            username=data['email'],
        )
        student = Student(user=user, phone_number=data['phone_number'])
        student.save()
