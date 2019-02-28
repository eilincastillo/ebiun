"""Service urls"""

# Django
from django.urls import path

# View
from .views import regular_class, special_class, accredited_training, rent_of_rooms, new_service


urlpatterns =[
    path(route='clases-regulares/',
         view=regular_class,
         name='regular_class' ),

    path(route='clases-especiales/',
         view=special_class,
         name='special_class'),

    path(route='formaciones-acreditadas/',
         view=accredited_training,
         name='accredited_training'),

    path(route='renta-de-salones/',
         view=rent_of_rooms,
         name='rent_of_rooms'),

    path(route='nuevo-servicio/',
         view=new_service,
         name='new_service'),
]
