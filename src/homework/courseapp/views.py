from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from userapp.models import Teacher, User

from .forms import CourseInfoForm
from .models import Course
# Create your views here.


class TeacherCoursesView(LoginRequiredMixin, generic.ListView):
    template_name = 'courseapp/teacher_courses.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Teacher.objects.get(pk=self.request.user.id).course_set.all()

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'My courses'})
        return cxt


class NewCourseView(LoginRequiredMixin, UserPassesTestMixin,
                    generic.CreateView):
    template_name = 'courseapp/new_course.html'
    form_class = CourseInfoForm
    success_url = reverse_lazy('courseapp:teacher_courses')

    def test_func(self):
        return self.request.user.user_type == User.Types.TEACHER

    def form_valid(self, form):
        course = form.save(commit=False)
        course.teacher = self.request.user
        course.save()
        return redirect(reverse('courseapp:teacher_courses'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'New course'})
        return cxt


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courseapp/course_details.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.name})
        return cxt


class CourseUpdateView(generic.UpdateView):
    model = Course
    form_class = CourseInfoForm
    template_name = 'courseapp/update_course.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.name})
        return cxt
