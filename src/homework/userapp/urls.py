from django.urls import path

from . import views

app_name = 'userapp'

urlpatterns = [
    path('register/', views.register, name='register')
]
