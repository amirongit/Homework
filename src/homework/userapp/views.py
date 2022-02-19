from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm
from .models import Teacher, Student

# Create your views here.


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid() is not True:
            return render(request, 'main/error.html',
                          {'title': 'Form Validation',
                           'error': 'The form wasn\'t filled out properly.'})
        model = Teacher if reg_form.cleaned_data[
            'user_type'] == 't' else Student
        try:
            model.objects.create_user(
                username=reg_form.cleaned_data['username'],
                first_name=reg_form.cleaned_data['first_name'],
                last_name=reg_form.cleaned_data['last_name'],
                email=reg_form.cleaned_data['email'],
                password=reg_form.cleaned_data['password'])
        except (IntegrityError, ValueError):
            return render(request, 'main/error.html',
                          {'title': 'Value Error',
                           'error': 'The given values can\'t be used.'})
        return redirect(reverse('interface:index'))
    reg_form = RegisterForm()
    return render(request, 'userapp/register.html', {'title': 'Register',
                                                     'reg_form': reg_form})
