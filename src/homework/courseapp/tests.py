from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now
from userapp.models import Teacher

from .models import Course, Presentation

# Create your tests here.


class CourseModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', first_name='Dummy',
                               last_name='Teacher')
        Course.objects.create(name='Dummy Course',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'))

    def test_string_format(self):
        self.assertEqual(str(Course.objects.get(name='Dummy Course')),
                         'Dummy Course by Teacher: Dummy Teacher')


class PresentationModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(username='dummyteacher', first_name='Dummy',
                               last_name='Teacher')
        Course.objects.create(name='Dummy Course',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'))
        Presentation.objects.create(start_date=now().date() -
                                    timedelta(days=3),
                                    end_date=now().date() + timedelta(days=3),
                                    course=Course.objects.get(
                                        name='Dummy Course'))

    def test_string_format(self):
        presentation_obj = Presentation.objects.get(pk=1)
        self.assertEqual(str(presentation_obj),
                         f'{str(presentation_obj.course)} from '
                         f'{str(now().date() - timedelta(days=3))} to '
                         f'{str(now().date() + timedelta(days=3))}')
