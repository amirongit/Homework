from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Course(models.Model):
    name = models.CharField('course name', max_length=128, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    teacher = models.ForeignKey('userapp.Teacher', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('courseapp:course_details', kwargs={'pk': self.id})

    def get_active_presentations(self):
        return self.presentation_set.filter(start_date__lte=now().date(), end_date__gte=now().date())

    def get_attendable_presentations(self):
        return self.presentation_set.filter(start_date__gte=now().date())


class PresentationStudentRel(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['student', 'presentation'], name='unique attendancy')]

    student = models.ForeignKey('userapp.Student', on_delete=models.CASCADE)
    presentation = models.ForeignKey('courseapp.Presentation', on_delete=models.CASCADE)
    grade = models.IntegerField(blank=False, null=False, default=0)

    def get_absolute_url(self):
        return reverse('courseapp:attendancy_details', kwargs={'pk': self.id})


class Presentation(models.Model):
    start_date = models.DateField('start date', null=False, blank=False)
    end_date = models.DateField('end date', null=False, blank=False)
    course = models.ForeignKey('courseapp.Course', on_delete=models.CASCADE, null=False, blank=False)
    students = models.ManyToManyField('userapp.Student', through=PresentationStudentRel)

    def is_active(self):
        return (self.start_date <= now().date()) and (self.end_date >= now().date())

    def is_attendable(self):
        return self.start_date >= now().date()

    def __str__(self):
        return f'{str(self.course)}: {self.start_date} - {self.end_date}'


class HomeworkStudentRel(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['student', 'homework'], name='unique answer')]

    student = models.ForeignKey('userapp.Student', on_delete=models.CASCADE, blank=False, null=False)
    homework = models.ForeignKey('courseapp.Homework', on_delete=models.CASCADE, blank=False, null=False)
    answer = models.TextField(blank=False, null=False)


class Homework(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    presentation = models.ForeignKey('courseapp.Presentation', on_delete=models.CASCADE, blank=False, null=False)
    answers = models.ManyToManyField('userapp.Student', through=HomeworkStudentRel)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    presentation = models.ForeignKey('courseapp.Presentation', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
