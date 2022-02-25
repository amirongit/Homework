from django.urls import path, include

from . import views

app_name = 'courseapp'

urlpatterns = [
    path('teacher/', include([
        path('courses/', views.TeacherCoursesView.as_view(),
             name='teacher_courses'),
        path('new_course/', views.NewCourseView.as_view(),
             name='teacher_new_course')
    ])),
    path('student/', include([
    ]))
]
