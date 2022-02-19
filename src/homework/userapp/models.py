from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Teacher(User):
    pass


class Student(User):
    pass
