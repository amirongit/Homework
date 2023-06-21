from django.urls import include, path

from . import views

app_name = 'courseapp'

urlpatterns = [
    path(
        'teacher/',
        include(
            [
               path('courses/', views.TeacherCoursesView.as_view(), name='teacher_courses'),
               path('new_course/', views.NewCourseView.as_view(), name='new_course'),
               path('update_course/<int:pk>/', views.CourseUpdateView.as_view(), name='update_course'),
               path('new_presentation/<int:course_id>/', views.NewPresentationView.as_view(), name='new_presentation'),
               path(
                   'course_presentations/<int:pk>/',
                   views.CoursePresentationsView.as_view(),
                   name='course_presentations'
               ),
               path(
                   'manage_presentation/<int:pk>/',
                   views.ManagePresentationView.as_view(),
                   name='manage_presentation'
               ),
               path('new_homework/<int:presentation_id>/', views.NewHomeworkView.as_view(), name='new_homework'),
               path('homework_details/<int:pk>/', views.HomeworkDetailsView.as_view(), name='homework_details'),
               path('update_grade/<int:pk>/', views.UpdateGradeView.as_view(), name='update_grade'),
               path('attendancy_details/<int:pk>/', views.AttendancyDetailsView.as_view(), name='attendancy_details'),
               path('new_lecture/<int:presentation_id>/', views.NewLectureView.as_view(), name='new_lecture')
            ]
        )
    ),
    path(
        'student/',
        include(
          [
              path('join_presentation/<int:pk>/', views.JoinPresentationView.as_view(), name='join_presentation'),
              path('submit_answer/<int:homework_id>/', views.SubmitAnswerView.as_view(), name='submit_answer'),
              path('courses/', views.StudentCoursesView.as_view(), name='student_courses'),
              path('course_dashboard/<int:pk>/', views.PresentationDashboardView.as_view(), name='course_dashboard')
          ]
        )
     ),
    path('course_details/<int:pk>/', views.CourseDetailsView.as_view(), name='course_details'),
    path('lecture_details/<int:pk>/', views.LectureDetailsView.as_view(), name='lecture_details'),
    path(
        'certificate_details/<int:presentation_id>/<int:student_id>/',
        views.CertificateDetailsView.as_view(),
        name='certificate_details'
     )
]
