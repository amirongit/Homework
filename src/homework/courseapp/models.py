from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField('course name', max_length=128)
    description = models.TextField(blank=False, null=False)
    teacher = models.ForeignKey('userapp.Teacher', on_delete=models.CASCADE,
                                null=False, blank=False)

    def __str__(self):
        return f'{self.name} by {str(self.teacher)}'


class PresentationStudentRel(models.Model):
    student = models.ForeignKey('userapp.Student', on_delete=models.CASCADE)
    presentation = models.ForeignKey('courseapp.Presentation',
                                     on_delete=models.CASCADE)
    grade = models.IntegerField('course grade', blank=True, null=True)


class Presentation(models.Model):
    start_date = models.DateField('start date', null=False, blank=False)
    end_date = models.DateField('end date', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False,
                               blank=False)
    students = models.ManyToManyField('userapp.Student',
                                      through=PresentationStudentRel)

    def __str__(self):
        return f'{str(self.course)} from {self.start_date} to {self.end_date}'
