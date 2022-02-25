from django.forms import ModelForm

from .models import Course


class CourseInfoForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['teacher']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
