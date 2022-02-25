from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin, AccessMixin)
from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import SignUpForm, SignInForm

# Create your views here.


@user_passes_test(lambda user: user.is_anonymous)
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return redirect(reverse('userapp:sign_up'))
        try:
            form.save()
            return redirect(reverse('userapp:sign_in'))
        except (IntegrityError, ValueError):
            return redirect(reverse('userapp:sign_up'))
    form = SignUpForm()
    return render(request, 'userapp/sign_up.html', {'title': 'Sign up',
                                                    'form': form})


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
