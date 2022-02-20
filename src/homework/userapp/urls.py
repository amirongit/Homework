from django.urls import path

from . import views

app_name = 'userapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginView_.as_view(), name='login'),
    path('logout/', views.LogoutView_.as_view(), name='logout')
]
