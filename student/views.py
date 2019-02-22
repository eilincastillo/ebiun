"""Student views."""

# Django
from django.shortcuts import render, redirect

# Forms
from student.forms import SignupForm

# Models
from student.models import Student
from services.models import Service


def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignupForm

    return render(
        request=request,
        template_name='student/signup.html',
        context={
            'form':form
        }
    )


def dashboard(request):
    """Dashboard student view"""
    student = Student.objects.get(user_id=request.user.id)
    student_services = student.service.all()
    services = Service.objects.all().exclude(id__in=student_services)

    return render(
        request=request,
        template_name='student/dashboardStudent.html',
        context={
            'student':student,
            'student_services':student_services,
            'services':services
        }
    )


def signup_class(request, id):
    """Singn up class view"""
    id_user = None
    if request.user.is_authenticated:
        id_user = request.user.id
    student = Student.objects.get(user_id=id_user)
    service = Service.objects.get(id=id)

    student.service.add(service)

    # student = Student.objects.get(user_id=id)
    student_services = student.service.all()
    services = Service.objects.all().exclude(id__in=student_services)


    return render(
        request=request,
        template_name='student/dashboardStudent.html',
        context={
            'student': student,
            'student_services': student_services,
            'services': services
        }
    )

