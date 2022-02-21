from django.test import TestCase
from django.urls import reverse

from .utils import create_student


class RegisterViewTest(TestCase):
    def setUp(self):
        create_student()

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
                               data={'username': 'dummystudent',
                                     'password1': 'dummypassword',
                                     'password2': 'dummypassword',
                                     'email': 'newuser@email.com',
                                     'first_name': 'New', 'last_name': 'User',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:register'))


class LoginViewTest(TestCase):
    def test_get(self):
        res = self.client.get(reverse('userapp:login'))
        self.assertContains(res, '<title>Homework - Login</title>',
                            html=True)
