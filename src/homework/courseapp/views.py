from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from userapp.models import Student, Teacher, User
from userapp.utils import StudentOnlyViewMixin, TeacherOnlyViewMixin

from .forms import (AnswerSubmitionForm, CourseInfoForm, GradeUpdateForm,
                    HomeworkCreationForm, LectureInforForm,
                    PresentationCreationForm)
from .models import (Course, Homework, HomeworkStudentRel, Lecture,
                     Presentation, PresentationStudentRel)

# Create your views here.


class TeacherCoursesView(TeacherOnlyViewMixin, generic.ListView):
    template_name = 'courseapp/teacher_courses.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Teacher.objects.get(pk=self.request.user.id).course_set.all()

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Courses'})
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
        if (not self.request.user.is_anonymous) and (
                self.request.user.user_type == User.Types.STUDENT
                ):
            taken = Student.objects.get(id=self.request.user.id).has_taken(
                Course.objects.get(id=self.object.id)
                )
            cxt.update({'taken': taken})
        cxt.update({'title': self.object.name})
        return cxt


class CourseUpdateView(TeacherOnlyViewMixin, generic.UpdateView):
    model = Course
    form_class = CourseInfoForm
    template_name = 'courseapp/update_course.html'

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return self.get_object().teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.name})
        return cxt


class NewPresentationView(TeacherOnlyViewMixin, generic.CreateView):
    template_name = 'courseapp/new_presentation.html'
    form_class = PresentationCreationForm

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return Course.objects.get(id=self.kwargs[
                'course_id'
                ]).teacher == self.request.user
        return False

    def form_valid(self, form):
        presentation = form.save(commit=False)
        presentation.course = Course.objects.get(id=self.kwargs['course_id'])
        presentation.save()
        return redirect(
            reverse('courseapp:course_presentations', kwargs=(
                {'pk': self.kwargs['course_id']}
                ))
                )

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update(
            {'title': 'New presentation', 'course_name': Course.objects.get(
                id=self.kwargs['course_id']
                ).name}
                    )
        return cxt


class CoursePresentationsView(TeacherOnlyViewMixin, generic.ListView):
    template_name = 'courseapp/course_presentations.html'
    context_object_name = 'presentation_set'

    def get_queryset(self):
        return Course.objects.get(id=self.kwargs['pk']).presentation_set.all()

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return Course.objects.get(id=self.kwargs[
                'pk'
                ]).teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': Course.objects.get(id=self.kwargs['pk']).name,
                    'course_id': self.kwargs['pk']})
        return cxt


class JoinPresentationView(StudentOnlyViewMixin, generic.View):
    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            student = Student.objects.get(id=self.request.user.id)
            presentation = Presentation.objects.get(id=self.kwargs['pk'])
            return (not student.has_attended(presentation)) and (
                not student.has_taken(presentation.course)
                )
        return False

    def get(self, request, pk):
        presentation = Presentation.objects.get(id=pk)
        student = Student.objects.get(id=request.user.id)
        rel_obj = PresentationStudentRel(
            student=student, presentation=presentation
            )
        try:
            rel_obj.save()
            return redirect(reverse('courseapp:student_courses'))
        except IntegrityError:
            return redirect(reverse('courseapp:course_details', kwargs={
                                        'pk': presentation.course.id
                                            })
                            )


class ManagePresentationView(TeacherOnlyViewMixin, generic.DetailView):
    model = Presentation
    template_name = 'courseapp/manage_presentation.html'

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return self.get_object().course.teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.course.name})
        return cxt


class NewHomeworkView(TeacherOnlyViewMixin, generic.CreateView):
    model = Homework
    template_name = 'courseapp/new_homework.html'
    form_class = HomeworkCreationForm

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return Presentation.objects.get(id=self.kwargs[
                'presentation_id'
                ]).course.teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'New homework'})
        return cxt

    def form_valid(self, form):
        homework = form.save(commit=False)
        homework.presentation = Presentation.objects.get(id=self.kwargs[
            'presentation_id'
            ])
        homework.save()
        return redirect(reverse('courseapp:manage_presentation', kwargs={
            'pk': self.kwargs['presentation_id']
            }))


class SubmitAnswerView(StudentOnlyViewMixin, generic.CreateView):
    model = HomeworkStudentRel
    template_name = 'courseapp/submit_answer.html'
    form_class = AnswerSubmitionForm

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            homework = Homework.objects.get(id=self.kwargs['homework_id'])
            student = Student.objects.get(id=self.request.user.id)
            return (student.has_attended(homework.presentation)) and (
                not HomeworkStudentRel.objects.filter(
                    homework=homework
                    ).filter(student=student).exists()
                )
        return False

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.homework = Homework.objects.get(id=self.kwargs['homework_id'])
        answer.student = Student.objects.get(id=self.request.user.id)
        answer.save()
        return redirect('/')  # change to the list of homeworks later

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({
            'title': f'{Homework.objects.get(id=self.kwargs["homework_id"])}'
            })
        return cxt


class HomeworkDetailsView(TeacherOnlyViewMixin, generic.DetailView):
    model = Homework
    template_name = 'courseapp/homework_details.html'

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return self.get_object(
            ).presentation.course.teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': f'{self.get_object().title}'})
        return cxt


class UpdateGradeView(TeacherOnlyViewMixin, generic.UpdateView):
    model = PresentationStudentRel
    form_class = GradeUpdateForm
    template_name = 'courseapp/update_grade.html'

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return self.get_object(
            ).presentation.course.teacher.id == self.request.user.id
        return False

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': f'Update {self.get_object().student}'})
        return cxt


class AttendancyDetailsView(TeacherOnlyViewMixin, generic.DetailView):
    model = PresentationStudentRel
    template_name = 'courseapp/attendancy_details.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({
                    'title': f'{self.get_object().student}',
                    'homework_set': HomeworkStudentRel.objects.filter(
                        homework__presentation=self.get_object().presentation
                        ).filter(student=self.get_object().student)
                })
        return cxt


class StudentCoursesView(StudentOnlyViewMixin, generic.ListView):
    template_name = 'courseapp/student_courses.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Presentation.objects.filter(
            presentationstudentrel__student=Student.objects.get(
                id=self.request.user.id
            )
            )

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Courses'})
        return cxt


class PresentationDashboardView(StudentOnlyViewMixin, generic.DetailView):
    model = Presentation
    template_name = 'courseapp/presentation_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.get_object().course.name,
                    'student': Student.objects.get(id=self.request.user.id)})
        return cxt


class NewLectureView(TeacherOnlyViewMixin, generic.CreateView):
    template_name = 'courseapp/new_lecture.html'
    form_class = LectureInforForm

    def test_func(self, *args, **kwargs):
        if super().test_func(*args, **kwargs):
            return Presentation.objects.get(id=self.kwargs[
                'presentation_id'
                ]).course.teacher.id == self.request.user.id
        return False

    def form_valid(self, form):
        lecture = form.save(commit=False)
        lecture.presentation = Presentation.objects.get(id=self.kwargs[
            'presentation_id'
            ])
        lecture.save()
        return redirect(reverse('courseapp:manage_presentation', kwargs={
            'pk': self.kwargs['presentation_id']
            }))

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'New lecture'})
        return cxt


class LectureDetailsView(generic.DetailView):
    model = Lecture
    template_name = 'courseapp/lecture_details.html'

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': self.object.title})
        return cxt
