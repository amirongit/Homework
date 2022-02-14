from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField('course name', max_length=128)
    teacher = models.ForeignKey('userapp.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.creator.name}'


class PersentationStudentRel(models.Model):
    student = models.ForeignKey('userapp.Student', on_delete=models.CASCADE)
    # TODO: if the student object is deleted, will it cause the presentation
    # object to delete?!
    presentation = models.ForeignKey('courseapp.Presentation',
                                     on_delete=models.CASCADE)
    grade = models.IntegerField('course grade', blank=True)
    passed = models.BooleanField(default=False)


class Presentation(models.Model):
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField('userapp.Student',
                                      through=PersentationStudentRel)

    def __str__(self):
        return f'{str(self.course)} from {self.start_date} to {self.end_date}'
