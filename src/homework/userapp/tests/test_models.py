from django.test import TestCase

from ..models import Student, Teacher, User
from .utils import create_student, create_teacher, create_user


class UserModelTest(TestCase):
    def setUp(self):
        create_user(user_type=User.Types.TEACHER)

    def test_string_format(self):
        self.assertEqual(str(User.objects.get(username='dummyuser')),
                         'Teacher: Dummy User')


class TeacherModelTest(TestCase):
    def setUp(self):
        create_teacher()

    def test_queryset(self):
        self.assertEqual(Teacher.objects.all()[0].user_type,
                         User.Types.TEACHER)


class StudentModelTest(TestCase):
    def setUp(self):
        create_student()

    def test_queryset(self):
        self.assertEqual(Student.objects.all()[0].user_type,
                         User.Types.STUDENT)
