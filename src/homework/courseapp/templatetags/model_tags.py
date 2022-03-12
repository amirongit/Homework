from django.template import Library
from django.utils.timezone import now

register = Library()


def student_has_answered(student, homework):
    return student.has_answered(homework)


register.filter('student_has_answered', student_has_answered)


def presentation_has_ended(presentation):
    return presentation.end_date < now().date()


register.filter('presentation_has_ended', presentation_has_ended)
