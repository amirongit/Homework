from django.test import TestCase

from .models import User, Teacher, Student

# Create your tests here.


class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='dummyuser',
                                 email='dummyuser@email.com',
                                 password='dummypassword', first_name='Dummy',
                                 last_name='User',
                                 user_type=User.Types.TEACHER)

    def test_string_format(self):
        self.assertEqual(str(User.objects.get(username='dummyuser')),
                         'Teacher: Dummy User')


class TeacherModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create_user(username='dummyuser',
                                    email='dummyuser@email.com',
                                    password='dummypassword',
                                    first_name='Dummy',
                                    last_name='User')

    def test_teacher_manager_queryset(self):
        self.assertEqual(Teacher.objects.all()[0].user_type,
                         User.Types.TEACHER)


class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create_user(username='dummyuser',
                                    email='dummyuser@email.com',
                                    password='dummypassword',
                                    first_name='Dummy',
                                    last_name='User')

    def test_student_manager_queryset(self):
        self.assertEqual(Student.objects.all()[0].user_type,
                         User.Types.STUDENT)
