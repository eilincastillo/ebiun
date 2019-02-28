"""Services forms"""

# Django
from django import forms

# Model
from .models import Service



class NewServiceForm(forms.Form):
    """Contact form"""
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    type = forms.CharField(max_length=20, required=True)
    benefit = forms.CharField(widget=forms.Textarea, required=False)
    length = forms.CharField(max_length=10, required=True)
    capacity = forms.CharField(max_length=10, required=True)

    def clean_name(self):
        """Username must be unique"""
        name = self.cleaned_data['name']
        name_taken = Service.objects.filter(name=name).exists()

        if name_taken:
            raise forms.ValidationError('Esta clase ya esta registrada')
        return name

    def save(self):
        """Create a new service"""
        data = self.cleaned_data

        service = Service.objects.create(
            name=data['name'],
            description=data['description'],
            type=data['type'],
            benefit=data['benefit'],
            length=data['length'],
            capacity=data['capacity'],
        )
        service.save()

