from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from userapp.models import Teacher
# Create your views here.


class TeacherCoursesView(LoginRequiredMixin, generic.ListView):
    template_name = 'courseapp/teacher_courses.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Teacher.objects.get(pk=self.request.user.id).course_set.all()
