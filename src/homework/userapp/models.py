from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from courseapp.models import PresentationStudentRel
# Create your models here.


class User(AbstractUser):
    objects = UserManager()

    class Types(models.TextChoices):
        TEACHER = ('TEACHER', 'Teacher')
        STUDENT = ('STUDENT', 'Student')

    user_type = models.CharField(max_length=8, choices=Types.choices,
                                 null=False, blank=False)

    def __str__(self):
        return f'{self.get_user_type_display()}: \
{self.first_name} {self.last_name}'


class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user_type=User.Types.TEACHER)


class Teacher(User):
    class Meta:
        proxy = True

    objects = TeacherManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.Types.TEACHER
        super().save(*args, **kwargs)


class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user_type=User.Types.STUDENT)


class Student(User):
    class Meta:
        proxy = True

    objects = StudentManager()

    def has_attended(self, course):
        return PresentationStudentRel.objects.filter(
            presentation__course=course).filter(student=self).exists()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.Types.STUDENT
        super().save(*args, **kwargs)
