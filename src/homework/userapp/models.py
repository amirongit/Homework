from django.db import models

# Create your models here.


class User(models.Model):

    class Meta:
        abstract = True

    username = models.CharField('username', max_length=32, unique=True,
                                blank=False, null=False)
    name = models.CharField('real name', max_length=128, blank=False,
                            null=False)
    registration_date = models.DateField('registration date', null=False,
                                         auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(User):
    pass


class Student(User):
    pass
