from django.urls import path, include

from . import views

app_name = 'courseapp'

urlpatterns = [
    path('teacher/', include([
        path('courses/',
             views.TeacherCoursesView.as_view(),
             name='teacher_courses'),
        path('new_course/',
             views.NewCourseView.as_view(),
             name='new_course'),
        path('update_course/<int:pk>/',
             views.CourseUpdateView.as_view(),
             name='update_course'),
        path('new_presentation/<int:course_id>/',
             views.NewPresentationView.as_view(),
             name='new_presentation'),
        path('course_presentations/<int:pk>/',
             views.CoursePresentationsView.as_view(),
             name='course_presentations'),
        path('manage_presentation/<int:pk>/',
             views.ManagePresentationView.as_view(),
             name='manage_presentation')
             ])),
    path('student/', include([
         path('join_presentation/<int:pk>/',
              views.JoinPresentationView.as_view(),
              name='join_presentation')
         ])),
    path('course_details/<int:pk>/', views.CourseDetailsView.as_view(),
         name='course_details')
     ]
