"""Ebiun views"""

# Django
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms
from .forms import ContactForm, LoginForm

# Models
from student.models import Student
from services.models import Service


def index(request):
    """Index view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                'Correo de contactenos',
                'Un nuevo usuario se ha puesto en contacto contigo. \n\nNombre: '+data['name']+'\nCorreo de contacto: '+data['email']+'\nMensaje: '+data['message'],
                data['email'],  # FROM
                ['castilloeilin@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'index.html',{'form': form})


def login_user(request):
    """Login view"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(request, username=data['email'], password=data['password'])
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('student:dashboard')


            else:
                return render(request, 'login.html', {'error': 'Username o contraseña invalida'})
    else:
        form = LoginForm()

    return render(
        request=request,
        template_name= 'login.html',
        context= {
            'form': form
        })

# @login_required
def dashboard(request):
    """Dashboard view"""

    students = Student.objects.all()
    services = Service.objects.all()
    services_return = []

    for service in services:
        count_student_inscribed = Student.objects.filter(service__in=[service]).count()
        dictionary_service = {
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'type': service.type,
            'availability': str(service.capacity - count_student_inscribed)+' / '+str(service.capacity)
        }

        services_return.append(dictionary_service)


    return render(
        request=request,
        template_name='dashboardAdmin.html',
        context={
            'students': students,
            'services': services_return
        }
        )

