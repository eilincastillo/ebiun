"""Student urls"""

# Django
from django.urls import path

# View
from student import views


app_name = 'student'
urlpatterns =[
    path(route='registro/',
         view=views.signup,
         name='signup'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('signup-class/<int:id>/', views.signup_class, name='signupClass'),

    path('unsubscribe-class/<int:id>/', views.unsubscribe, name='unsubscribe'),

]
