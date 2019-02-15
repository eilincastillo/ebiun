"""Student views."""

# Django
from django.shortcuts import render, redirect

# Forms
from student.forms import SignupForm


def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = SignupForm

    return render(
        request=request,
        template_name='',
        context={
            'form':form
        }
    )
