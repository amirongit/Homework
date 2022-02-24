from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages import error, success

from userapp.models import Teacher, User

from .forms import CourseCreationForm
from .utils import generate_user_type_test
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


@user_passes_test(generate_user_type_test(User.Types.TEACHER))
def new_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if not form.is_valid():
            error(request, '* You didn\'t fill out the form properly.')
            return redirect(reverse('courseapp:teacher_new_course'))
        course = form.save(commit=False)
        course.teacher = request.user
        course.save()
        success(request, 'The course was added successfully.')
        return redirect(reverse('courseapp:teacher_courses'))
    form = CourseCreationForm()
    return render(request, 'courseapp/new_course.html',
                  {'title': 'New course', 'form': form})
