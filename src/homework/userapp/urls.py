from django.urls import path

from . import views

app_name = 'userapp'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.SingInView.as_view(), name='sign_in'),
    path('sign_out/', views.SignOutView.as_view(), name='sign_out'),
    path('profile/<int:pk>/', views.TeacherProfileView.as_view(), name='teacher_profile')
]
