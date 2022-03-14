from datetime import timedelta

from courseapp.models import Course, Homework, Presentation
from django.test import TestCase
from django.utils.timezone import now

from ..models import Student, Teacher, User


class TestUserModel(TestCase):
    def setUp(self):
        User.objects.create_user(username='dummyuser', first_name='Dummy',
                                 last_name='User', email='dummy@email.com',
                                 password='dummypassword')


class TestTeacherModel(TestCase):
    def setUp(self):
        Teacher.objects.create_user(username='dummyteacher',
                                    first_name='Dummy', last_name='Teacher',
                                    email='dummyt@email.com',
                                    password='dummypassword')

    def test_user_type_attribute(self):
        teacher = Teacher.objects.get(username='dummyteacher')
        self.assertEqual(teacher.user_type, User.Types.TEACHER)


class TestStudentModel(TestCase):
    def setUp(self):
        Student.objects.create_user(username='dummystudent',
                                    first_name='Dummy', last_name='Student',
                                    email='dummys@email.com',
                                    password='dummypassword')
        Teacher.objects.create_user(username='dummyteacher',
                                    first_name='Dummy', last_name='Teacher',
                                    email='dummyt@email.com',
                                    password='dummypassword')
        Course.objects.create(name='Dummy course',
                              description='Dummy description, '
                                          'just to be written.',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'
                              ))
        Presentation.objects.create(
            start_date=now().date() - timedelta(days=-1),
            end_date=now().date() + timedelta(days=1),
            course=Course.objects.get(name='Dummy course')
        )
        Presentation.objects.get(id=1).students.add(
            Student.objects.get(username='dummystudent')
        )
        Homework.objects.create(title='Dummy homework',
                                description='Dummy description, '
                                            'just to be written.',
                                presentation=Presentation.objects.get(id=1))
        Homework.objects.get(title='Dummy homework').answers.add(
            Student.objects.get(username='dummystudent'),
            through_defaults={'answer': 'Dummy answer, just to be written.'}
        )
        Homework.objects.create(title='Another dummy homework',
                                description='Dummy description, '
                                            'just to be written.',
                                presentation=Presentation.objects.get(id=1))
        Course.objects.create(name='Another dummy course',
                              description='Dummy description, '
                                          'just to be written.',
                              teacher=Teacher.objects.get(
                                  username='dummyteacher'
                              ))
        Presentation.objects.create(
            start_date=now().date() - timedelta(days=-1),
            end_date=now().date() + timedelta(days=1),
            course=Course.objects.get(name='Another dummy course')
        )

    def test_user_type_attribute(self):
        student = Student.objects.get(username='dummystudent')
        self.assertEqual(student.user_type, User.Types.STUDENT)

    def test_has_taken(self):
        student = Student.objects.get(username='dummystudent')
        course = Course.objects.get(name='Dummy course')
        another_course = Course.objects.get(name='Another dummy course')
        self.assertIs(student.has_taken(course), True)
        self.assertIs(student.has_taken(another_course), False)

    def test_has_attended(self):
        student = Student.objects.get(username='dummystudent')
        presentation = Presentation.objects.get(id=1)
        another_presentation = Presentation.objects.get(id=2)
        self.assertIs(student.has_attended(presentation), True)
        self.assertIs(student.has_attended(another_presentation), False)

    def test_has_answered(self):
        student = Student.objects.get(username='dummystudent')
        homework = Homework.objects.get(title='Dummy homework')
        another_homework = Homework.objects.get(title='Another dummy homework')
        self.assertIs(student.has_answered(homework), True)
        self.assertIs(student.has_answered(another_homework), False)
