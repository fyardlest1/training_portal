from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/<int:pk>/', views.trainer_detail, name='trainer_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
]