"""Services module"""


# Django
from django.db import models


class Service(models.Model):
    """Service model"""

    TYPE_CHOICES = (
        ('regular_class', 'Clases Regulares'),
        ('special_class', 'Clases Especiales'),
        ('accredited_training', 'Formaciones Acreditadas'),
        ('rent_rooms', 'Alquiler de Salones'),
    )

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    benefit = models.TextField(blank=True)
    length = models.CharField(max_length=10, blank=True)
    capacity = models.IntegerField(default=5)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return self.name



