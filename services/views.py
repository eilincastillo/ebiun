from django.shortcuts import render

def regularClass(request):
    return render(request, 'services/regularClass.html')


def specialClass(request):
    return render(request, 'services/specialClass.html')


def accreditedTraining(request):
    return render(request, 'services/accreditedTraining.html')

def rentOfRooms(request):
    return render(request, 'services/rentOfRooms.html')

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


