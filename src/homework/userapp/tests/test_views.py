from django.test import TestCase
from django.urls import reverse

from .utils import create_student


class SignUpViewTest(TestCase):
    def setUp(self):
        create_student()

    def test_get(self):
        res = self.client.get(reverse('userapp:sign_up'))
        self.assertContains(res, '<title>Homework - Sign up</title>',
                            html=True)

    def test_valid_form_post(self):
        res = self.client.post(reverse('userapp:sign_up'),
                               data={'username': 'newuser',
                                     'password1': 'dummypassword',
                                     'password2': 'dummypassword',
                                     'email': 'newuser@email.com',
                                     'first_name': 'New', 'last_name': 'User',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:sign_in'))

    def test_invalid_form_post(self):
        res = self.client.post(reverse('userapp:sign_up'),
                               data={'username': 'dummyuser',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:sign_up'))

    def test_duplicated_form_post(self):
        res = self.client.post(reverse('userapp:sign_up'),
                               data={'username': 'dummystudent',
                                     'password1': 'dummypassword',
                                     'password2': 'dummypassword',
                                     'email': 'newuser@email.com',
                                     'first_name': 'New', 'last_name': 'User',
                                     'user_type': 'STUDENT'})
        self.assertEqual(res['Location'], reverse('userapp:sign_up'))


class SignInViewTest(TestCase):
    def test_get(self):
        res = self.client.get(reverse('userapp:sign_in'))
        self.assertContains(res, '<title>Homework - Sign in</title>',
                            html=True)
