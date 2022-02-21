from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin, AccessMixin)
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages import success, error
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegisterForm

# Create your views here.


@user_passes_test(lambda user: user.is_anonymous)
def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid() is not True:
            error(request, 'The form wasn\'t filled out properly.')
            return redirect(reverse('userapp:register'))
        try:
            reg_form.save()
        except (IntegrityError, ValueError):
            error(request, 'The given values can\'t be used.')
            return redirect(reverse('userapp:register'))
        success(request, 'The user was created successfully.')
        return redirect(reverse('userapp:login'))
    reg_form = RegisterForm()
    return render(request, 'userapp/register.html', {'title': 'Register',
                                                     'form': reg_form})


class LoginView_(UserPassesTestMixin, AccessMixin, LoginView):
    template_name = 'userapp/login.html'

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect(reverse('interface:index'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Login'})
        return cxt


class LogoutView_(LoginRequiredMixin, LogoutView):
    pass


# TODO: profile view
