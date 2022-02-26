from django.urls import path, include

from . import views

app_name = 'courseapp'

urlpatterns = [
    path('teacher/', include([
        path('courses/', views.TeacherCoursesView.as_view(),
             name='teacher_courses'),
        path('new_course/', views.NewCourseView.as_view(),
             name='teacher_new_course'),
        path('course/', include([
          path('update/<int:pk>/', views.CourseUpdateView.as_view(),
               name='course_update'),
          path('new_presentation/<int:course_id>/',
               views.NewPresentationView.as_view(),
               name='course_new_presentation')
        ]))
    ])),
    path('student/', include([
    ])),
    path('course/', include([
        path('details/<int:pk>/', views.CourseDetailView.as_view(),
             name='course_details'),
    ])),
]
