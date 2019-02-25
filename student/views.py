"""Student views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
def signup_class(request, id):
    """Singn up class view"""
    id_user = None
    error = None
    if request.user.is_authenticated:
        id_user = request.user.id
    student = Student.objects.get(user_id=id_user)
    students = Student.objects.all()
    service = Service.objects.get(id=id)
    count_student_inscribed = Student.objects.filter(service__in=[service]).count()

    if count_student_inscribed < service.capacity:
        student.service.add(service)
    else:
        error = 'Lo sentimos la clase de '+service.name+' esta llena. Le invitamos a inscribirte en otra clase'

    # student = Student.objects.get(user_id=id)
    student_services = student.service.all()
    services = Service.objects.all().exclude(id__in=student_services)


    return render(
        request=request,
        template_name='student/dashboardStudent.html',
        context={
            'student': student,
            'student_services': student_services,
            'services': services,
            'error': error
        }
    )

@login_required
def unsubscribe(request, id):
    """Unsubscribe a service."""
    id_user = None
    if request.user.is_authenticated:
        id_user = request.user.id
    student = Student.objects.get(user_id=id_user)
    service = Service.objects.get(id=id)

    # if student.service.get(student__service__in=service):
    student.service.remove(service)

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

