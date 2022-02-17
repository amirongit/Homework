from datetime import timedelta, date

from django.test import TestCase
from django.utils.timezone import now

from .models import Course, Presentation, PersentationStudentRel
from userapp.models import Teacher, Student
# Create your tests here.


class CourseModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', name='Dummy Teacher')
        teacher_obj = Teacher.objects.get(username='dummyteacher')
        Course.objects.create(name='Dummy Course', teacher=teacher_obj)

    def test_datatype_of_fields(self):
        course_obj = Course.objects.get(name='Dummy Course')
        self.assertIsInstance(course_obj.name, str)
        self.assertIsInstance(course_obj.teacher, Teacher)

    def test_teacher_relationship(self):
        teacher_obj = Teacher.objects.get(username='dummyteacher')
        course_obj = Course.objects.get(name='Dummy Course')
        self.assertEqual(course_obj.teacher, teacher_obj)

    def test_string_format(self):
        course_obj = Course.objects.get(name='Dummy Course')
        self.assertEqual(str(course_obj), 'Dummy Course by Dummy Teacher')


class PresentationModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', name='Dummy Teacher')
        teacher_obj = Teacher.objects.get(username='dummyteacher')
        Course.objects.create(name='Dummy Course', teacher=teacher_obj)
        course_obj = Course.objects.get(name='Dummy Course')
        Presentation.objects.create(start_date=now().date() -
                                    timedelta(days=3),
                                    end_date=now().date() + timedelta(days=3),
                                    course=course_obj)
        presentation_obj = Presentation.objects.get(pk=1)
        Student.objects.create(username='dummystudent', name='Dummy Student')
        student_obj = Student.objects.get(username='dummystudent')
        PersentationStudentRel.objects.create(student=student_obj,
                                              presentation=presentation_obj)

    def test_datatype_of_fields(self):
        presentation_obj = Presentation.objects.get(pk=1)
        self.assertIsInstance(presentation_obj.start_date, date)
        self.assertIsInstance(presentation_obj.end_date, date)
        self.assertIsInstance(presentation_obj.course, Course)
        self.assertIsInstance(presentation_obj.students.get(pk=1), Student)

    def test_students_relationship(self):
        student_obj = Student.objects.get(username='dummystudent')
        presentation_obj = Presentation.objects.get(pk=1)
        self.assertEqual(presentation_obj.students.get(pk=1), student_obj)

    def test_string_format(self):
        presentation_obj = Presentation.objects.get(pk=1)
        self.assertEqual(str(presentation_obj),
                         f'{str(presentation_obj.course)} from '
                         f'{str(now().date() - timedelta(days=3))} to '
                         f'{str(now().date() + timedelta(days=3))}')
