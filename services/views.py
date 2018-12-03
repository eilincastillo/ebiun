from django.shortcuts import render


def regularClass(request):
    return render(request, 'services/regularClass.html')


def specialClass(request):
    return render(request, 'services/specialClass.html')


def accreditedTraining(request):
    return render(request, 'services/accreditedTraining.html')

def rentOfRooms(request):
    return render(request, 'services/rentOfRooms.html')
