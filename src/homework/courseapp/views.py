from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError

from userapp.models import Teacher, User, Student
from userapp.utils import StudnetOnlyViewMixin, TeacherOnlyViewMixin

from .forms import CourseInfoForm, PresentationCreationForm
from .models import Course, Presentation, PresentationStudentRel
# Create your views here.


class TeacherCoursesView(TeacherOnlyViewMixin, generic.ListView):
    template_name = 'courseapp/teacher_courses.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Teacher.objects.get(
            pk=self.request.user.id
            ).course_set.all()

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'My courses'})
        return cxt


class NewCourseView(TeacherOnlyViewMixin, generic.CreateView):
    template_name = 'courseapp/new_course.html'
    form_class = CourseInfoForm

    def form_valid(self, form):
        course = form.save(commit=False)
        course.teacher = self.request.user
        course.save()
        return redirect(reverse('courseapp:teacher_courses'))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'New course'})
        return cxt


class CourseDetailsView(generic.DetailView):
    model = Course
    template_name = 'courseapp/course_details.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        if (
            not self.request.user.is_anonymous) and (
                self.request.user.user_type == User.Types.STUDENT
                ):
            attended = Student.objects.get(
                id=self.request.user.id
                ).has_attended(Course.objects.get(
                    id=self.object.id
                    ))
        else:
            attended = False
        cxt.update({'title': self.object.name, 'attended': attended})
        return cxt


class CourseUpdateView(TeacherOnlyViewMixin, generic.UpdateView):
    model = Course
    form_class = CourseInfoForm
    template_name = 'courseapp/update_course.html'

    def test_func(self, *args, **kwargs):
        result = super().test_func(*args, **kwargs)
        return (
            self.get_object().teacher.id == self.request.user.id
            ) and result

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.name})
        return cxt


class NewPresentationView(TeacherOnlyViewMixin, generic.CreateView):
    template_name = 'courseapp/new_presentation.html'
    form_class = PresentationCreationForm

    def test_func(self, *args, **kwargs):
        result = super().test_func(*args, **kwargs)
        return (
            Course.objects.get(
                id=self.kwargs['course_id']
                ).teacher == self.request.user
                ) and result

    def form_valid(self, form):
        presentation = form.save(commit=False)
        presentation.course = Course.objects.get(id=self.kwargs['course_id'])
        presentation.save()
        return redirect(
            reverse(
                'courseapp:course_details',
                kwargs=({'pk': self.kwargs['course_id']})
                )
                )

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update(
            {'title': 'New presentation',
             'course_name': Course.objects.get(
                id=self.kwargs['course_id']
                ).name}
                    )
        return cxt


class CoursePresentationsView(TeacherOnlyViewMixin, generic.ListView):
    template_name = 'courseapp/course_presentations.html'
    context_object_name = 'presentation_set'

    def get_queryset(self):
        return Presentation.objects.filter(
            course=Course.objects.get(id=self.kwargs['pk']))

    def test_func(self, *args, **kwargs):
        result = super().test_func(*args, **kwargs)
        return (
            Course.objects.get(
                id=self.kwargs['pk']
                ).teacher.id == self.request.user.id
                ) and result

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': Course.objects.get(id=self.kwargs['pk']).name,
                    'course_id': self.kwargs['pk']})
        return cxt


class JoinPresentationView(StudnetOnlyViewMixin, generic.View):
    def test_func(self):
        return self.request.user.user_type == User.Types.STUDENT

    def get(self, request, pk):
        presentation = Presentation.objects.get(id=pk)
        student = Student.objects.get(id=request.user.id)
        rel_obj = PresentationStudentRel(
            student=student,
            presentation=presentation
            )
        try:
            rel_obj.save()
            return redirect('/')  # change to dashboard later
        except IntegrityError:
            return redirect(
                reverse(
                    'courseapp:course_details',
                    kwargs=({'pk': presentation.course.id})
                    )
                )
