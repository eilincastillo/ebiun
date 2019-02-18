"""Ebiun views"""

# Django
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms
from .forms import ContactForm, LoginForm


def index(request):
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(request, username=data['email'], password=data['password'])
            if user:
                login(request, user)
                return redirect('index')

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
