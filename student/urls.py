"""Student urls"""

# Django
from django.urls import path

# View
from .views import signup


urlpatterns =[
    path(route='registro/',
         view=signup,
         name='signup'),

]
