from django.conf.urls import url
from .views import regularClass, specialClass, accreditedTraining, rentOfRooms

urlpatterns =[
    url(r'clases-regulares$', regularClass),
    url(r'clases-especiales$', specialClass),
    url(r'formaciones-acreditadas$', accreditedTraining),
    url(r'renta-de-salones$', rentOfRooms)
]