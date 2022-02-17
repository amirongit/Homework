from django.test import TestCase

# Create your tests here.

from .models import Teacher, Student


class TeacherModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', name='Dummy Teacher')

    def test_string_format(self):
        self.assertEqual(str(Teacher.objects.get(username='dummyteacher')),
                         'Dummy Teacher')


class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create(username='dummystudent', name='Dummy Student')

    def test_string_format(self):
        self.assertEqual(str(Student.objects.get(username='dummystudent')),
                         'Dummy Student')
