from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class User(AbstractUser):
    objects = UserManager()


class Teacher(User):
    pass


class Student(User):
    pass
