from django.template import Library

register = Library()


def student_has_answered(student, homework):
    return student.has_answered(homework)


register.filter('student_has_answered', student_has_answered)
