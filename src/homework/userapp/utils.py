from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import User


class TeacherOnlyViewMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == User.Types.TEACHER


class StudnetOnlyViewMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == User.Types.TEACHER


class AnonymousOnlyViewMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous
