"""Student urls"""

# Django
from django.urls import path

# View
from student import views


urlpatterns =[
    path(route='registro/',
         view=views.signup,
         name='signup'),

    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),

]
