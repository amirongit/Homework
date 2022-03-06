from django.contrib.auth.mixins import (AccessMixin, LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import redirect
from django.urls import reverse

from .models import User


class TeacherOnlyViewMixin(LoginRequiredMixin, UserPassesTestMixin,
                           AccessMixin):
    def test_func(self):
        return self.request.user.user_type == User.Types.TEACHER

    def handle_no_permission(self):
        return redirect(reverse('userapp:sign_in'))


class StudentOnlyViewMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == User.Types.STUDENT

    def handle_no_permission(self):
        return redirect(reverse('userapp:sign_in'))


class AnonymousOnlyViewMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect(reverse('interface:index'))
