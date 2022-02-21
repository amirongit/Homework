from django.test import TestCase
from django.urls import reverse

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

    def test_queryset(self):
        self.assertEqual(Teacher.objects.all()[0].user_type,
                         User.Types.TEACHER)


class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create_user(username='dummyuser',
                                    email='dummyuser@email.com',
                                    password='dummypassword',
                                    first_name='Dummy',
                                    last_name='User')

    def test_queryset(self):
        self.assertEqual(Student.objects.all()[0].user_type,
                         User.Types.STUDENT)


class RegisterViewTest(TestCase):
    def setUp(self):
        Student.objects.create_user(username='dummyuser',
                                    email='dummyuser@email.com',
                                    password='dummypassword',
                                    first_name='Dummy',
                                    last_name='User')

    def test_get(self):
        res = self.client.get(reverse('userapp:register'))
        self.assertContains(res, '<title>Homework - Register</title>',
                            html=True)

    def test_valid_form_post(self):
        res = self.client.post(reverse('userapp:register'),
                               data={'username': 'newuser',
                                     'password1': 'dummypassword',
                                     'password2': 'dummypassword',
                                     'email': 'newuser@email.com',
                                     'first_name': 'New', 'last_name': 'User',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:login'))

    def test_invalid_form_post(self):
        res = self.client.post(reverse('userapp:register'),
                               data={'username': 'dummyuser',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:register'))

    def test_duplicated_form_post(self):
        res = self.client.post(reverse('userapp:register'),
                               data={'username': 'dummyuser',
                                     'password1': 'dummypassword',
                                     'password2': 'dummypassword',
                                     'email': 'newuser@email.com',
                                     'first_name': 'New', 'last_name': 'User',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:register'))


class LoginViewTest(TestCase):
    def setUp(self):
        Student.objects.create_user(username='dummyuser',
                                    email='dummyuser@email.com',
                                    password='dummypassword',
                                    first_name='Dummy',
                                    last_name='User')

    def test_get(self):
        res = self.client.get(reverse('userapp:login'))
        self.assertContains(res, '<title>Homework - Login</title>',
                            html=True)
