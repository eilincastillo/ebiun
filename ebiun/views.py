from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect


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
