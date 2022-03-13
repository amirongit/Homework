from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from .forms import SignInForm, UserInfoForm
from .models import Teacher
from .utils import AnonymousOnlyViewMixin

# Create your views here.


class SignUpView(AnonymousOnlyViewMixin, generic.CreateView):
    template_name = 'userapp/sign_up.html'
    form_class = UserInfoForm
    success_url = reverse_lazy('userapp:sign_in')

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign up'})
        return cxt


class SingInView(AnonymousOnlyViewMixin, LoginView):
    template_name = 'userapp/sign_in.html'
    form_class = SignInForm

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Sign in'})
        return cxt


class SignOutView(LoginRequiredMixin, LogoutView):
    pass


class TeacherProfileView(generic.DetailView):
    model = Teacher
    template_name = 'userapp/teacher_profile.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update(
            {
                'title': f'{self.object.first_name} {self.object.last_name}'
            }
        )
        return cxt
