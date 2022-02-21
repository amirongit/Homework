from django.urls import path

from . import views

app_name = 'courseapp'

urlpatterns = [
    path('teacher_courses/', views.TeacherCoursesView.as_view(),
         name='teacher_courses'),
    path('course_create/', views.course_create, name='course_create')
]
