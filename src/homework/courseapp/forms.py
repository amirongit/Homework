from django.forms import ModelForm

from .models import Course


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['teacher']
