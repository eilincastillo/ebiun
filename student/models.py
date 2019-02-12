"""Student model"""

# Djngo
from django.db import models
from django.contrib.auth.models import User

# Models
from services.models import Service

class Student(models.Model):
    """Student model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, blank=True)

    service = models.ManyToManyField(Service)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

