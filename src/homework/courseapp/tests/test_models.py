from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from userapp.models import Teacher
from ..models import Course, Presentation


class TestCourseModel(TestCase):
    def setUp(self):
        Teacher.objects.create_user(username='dummyteacher',
                                    first_name='Dummy', last_name='Teacher',
                                    email='dummyt@email.com',
                                    password='dummypassword')
        Course.objects.create(name='Dummy course',
                              description='Dummy description just to be '
                                          'written.',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'
                              ))
        Presentation.objects.create(
            start_date=now().date() + timedelta(days=1),
            end_date=now().date() + timedelta(days=10),
            course=Course.objects.get(name='Dummy course')
        )
        Presentation.objects.create(
            start_date=now().date() - timedelta(days=1),
            end_date=now().date() + timedelta(days=10),
            course=Course.objects.get(name='Dummy course')
        )
        Presentation.objects.create(
            start_date=now().date() - timedelta(days=20),
            end_date=now().date() - timedelta(days=5),
            course=Course.objects.get(name='Dummy course')
        )

    def test_get_active_presentations(self):
        course = Course.objects.get(name='Dummy course')
        active_presentation = Presentation.objects.get(id=2)
        inactive_presentation = Presentation.objects.get(id=1)
        another_inactive_presentation = Presentation.objects.get(id=3)
        query_set = course.get_active_presentations()
        self.assertIn(active_presentation, query_set)
        self.assertNotIn(inactive_presentation, query_set)
        self.assertNotIn(another_inactive_presentation, query_set)

    def test_get_attendable_presentations(self):
        course = Course.objects.get(name='Dummy course')
        attendable_presentation = Presentation.objects.get(id=1)
        unattendable_presentation = Presentation.objects.get(id=2)
        another_unattendable_presentation = Presentation.objects.get(id=3)
        query_set = course.get_attendable_presentations()
        self.assertIn(attendable_presentation, query_set)
        self.assertNotIn(unattendable_presentation, query_set)
        self.assertNotIn(another_unattendable_presentation, query_set)


class TestPresentationModel(TestCase):
    def setUp(self):
        Teacher.objects.create_user(username='dummyteacher',
                                    first_name='Dummy', last_name='Teacher',
                                    email='dummyt@email.com',
                                    password='dummypassword')
        Course.objects.create(name='Dummy course',
                              description='Dummy description just to be '
                                          'written.',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'
                              ))
        Presentation.objects.create(
            start_date=now().date() + timedelta(days=1),
            end_date=now().date() + timedelta(days=10),
            course=Course.objects.get(name='Dummy course')
        )
        Presentation.objects.create(
            start_date=now().date() - timedelta(days=1),
            end_date=now().date() + timedelta(days=10),
            course=Course.objects.get(name='Dummy course')
        )

    def test_is_active(self):
        active_presentation = Presentation.objects.get(id=2)
        inactive_presentation = Presentation.objects.get(id=1)
        self.assertIs(active_presentation.is_active(), True)
        self.assertIs(inactive_presentation.is_active(), False)

    def test_is_attendable(self):
        attendable_presentation = Presentation.objects.get(id=1)
        unattendable_presentation = Presentation.objects.get(id=2)
        self.assertIs(attendable_presentation.is_attendable(), True)
        self.assertIs(unattendable_presentation.is_attendable(), False)
