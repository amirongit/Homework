from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import UserInfoForm, SignInForm
from .utils import AnonymousOnlyViewMixin

# Create your views here.


class SignUpView(AnonymousOnlyViewMixin, generic.CreateView):
    template_name = 'userapp/sign_up.html'
    form_class = UserInfoForm
    success_url = reverse_lazy('userapp:sign_in')

    def handle_no_permission(self):
        return redirect(reverse('interface:index'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign up'})
        return cxt


class SingInView(AnonymousOnlyViewMixin, AccessMixin, LoginView):
    template_name = 'userapp/sign_in.html'
    form_class = SignInForm

    def handle_no_permission(self):
        return redirect(reverse('interface:index'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign in'})
        return cxt


class SignOutView(LoginRequiredMixin, LogoutView):
    pass


# TODO: profile view
