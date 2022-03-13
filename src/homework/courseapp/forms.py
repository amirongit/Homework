from django import forms

from .models import (Course, Homework, HomeworkStudentRel, Lecture,
                     Presentation, PresentationStudentRel)


class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['teacher']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )


class LectureInforForm(forms.ModelForm):
    class Meta:
        model = Lecture
        exclude = ['presentation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})


class PresentationCreationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        exclude = ['students', 'course']

    start_date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'}
        )
    )
    end_date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'}
        )
    )


class HomeworkCreationForm(forms.ModelForm):
    class Meta:
        model = Homework
        exclude = ['presentation', 'answers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )


class AnswerSubmitionForm(forms.ModelForm):
    class Meta:
        model = HomeworkStudentRel
        exclude = ['student', 'homework']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs.update(
            {'class': 'form-control'}
        )


class GradeUpdateForm(forms.ModelForm):
    class Meta:
        model = PresentationStudentRel
        exclude = ['student', 'presentation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].widget.attrs.update({'class': 'form-control'})
