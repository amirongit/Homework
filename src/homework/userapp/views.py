from django.contrib.auth.views import LoginView
from django.contrib.messages import success, error
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegisterForm
from .models import Student, Teacher

# Create your views here.


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid() is not True:
            error(request, 'The form wasn\'t filled out properly.')
            return redirect(reverse('userapp:register'))
        user_type = Teacher if reg_form.cleaned_data[
            'user_type'] == 't' else Student
        try:
            user_type(user_ptr=reg_form.save()).save_base(raw=True)
        except (IntegrityError, ValueError):
            error(request, 'The given values can\'t be used.')
            return redirect(reverse('userapp:register'))
        success(request, 'The user was created succesfully.')
        return redirect(reverse('userapp:login'))
    reg_form = RegisterForm()
    return render(request, 'userapp/register.html', {'title': 'Register',
                                                     'form': reg_form})


class LoginView_(LoginView):
    template_name = 'userapp/login.html'
    # TODO: find out if the user is a teacher or a student and save it in a
    # session, remove login / view buttons from navbar for the logged in user
