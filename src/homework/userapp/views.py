from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin, AccessMixin)
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import UserInfoForm, SignInForm

# Create your views here.


class SignUpView(UserPassesTestMixin, generic.CreateView):
    template_name = 'userapp/sign_up.html'
    form_class = UserInfoForm
    success_url = reverse_lazy('userapp:sign_in')

    def test_func(self):
        return self.request.user.is_anonymous

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign up'})
        return cxt


class SingInView(UserPassesTestMixin, AccessMixin, LoginView):
    template_name = 'userapp/sign_in.html'
    form_class = SignInForm

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect(reverse('interface:index'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign in'})
        return cxt


class SignOutView(LoginRequiredMixin, LogoutView):
    pass


# TODO: profile view
