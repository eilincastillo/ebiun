"""Services view"""

# Django
from django.shortcuts import render

# Model
from services.models import Service


def regular_class(request):
    services = find_services(type_name='regular_class')
    return render(
        request=request,
        template_name='services/regularClass.html',
        context={
            'services': services
            })


def special_class(request):
    services = find_services(type_name='special_class')
    return render(
        request=request,
        template_name='services/specialClass.html',
        context={
            'services': services
            })


def accredited_training(request):
    return render(request, 'services/accreditedTraining.html')


def rent_of_rooms(request):
    return render(request, 'services/rentOfRooms.html')


def find_services(type_name):
    services = Service.objects.filter(type=type_name)
    return services

# def send_email(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             send_mail(
#                 'asunto',
#                 'mensaje',
#                 'castilloeilin@gmail.com',  # FROM
#                 'castilloeilin@gmail.com',
#                 fail_silently=False,
#             )
#             return HttpResponseRedirect('/')
#     else:
#         form = ContactForm()
#
#     return render(request, 'init/', {'form': form})


