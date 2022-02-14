from datetime import date

from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Teacher, Student


class TeacherModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', name='Dummy Teacher')

    def test_datatypes_of_fields(self):
        teacher_obj = Teacher.objects.get(username='dummyteacher')
        self.assertIsInstance(teacher_obj.username, str)
        self.assertIsInstance(teacher_obj.name, str)
        self.assertIsInstance(teacher_obj.registration_date, date)

    def test_value_of_registration_date_field(self):
        teacher_obj = Teacher.objects.get(username='dummyteacher')
        self.assertEqual(teacher_obj.registration_date, timezone.now().date())

    def test_string_format(self):
        self.assertEqual(str(Teacher.objects.get(username='dummyteacher')),
                         'Dummy Teacher')


class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create(username='dummystudent', name='Dummy Student')

    def test_datatypes_of_fields(self):
        student_obj = Student.objects.get(username='dummystudent')
        self.assertIsInstance(student_obj.username, str)
        self.assertIsInstance(student_obj.name, str)
        self.assertIsInstance(student_obj.registration_date, date)

    def test_value_of_registration_date_field(self):
        student_obj = Student.objects.get(username='dummystudent')
        self.assertEqual(student_obj.registration_date, timezone.now().date())

    def test_string_format(self):
        self.assertEqual(str(Student.objects.get(username='dummystudent')),
                         'Dummy Student')
