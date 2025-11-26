from django.urls import path
from . import views

urlpatterns = [
    # URLs for Course, Trainer, and Student views
    path('courses/', views.course_list, name='course_list'), # Step 1: List view for courses
    path('courses/<int:pk>/', views.course_detail, name='course_detail'), # Step 2: Detail view for a specific course
    path('trainers/', views.trainer_list, name='trainer_list'), # Step 1: List view for trainers
    path('trainers/<int:pk>/', views.trainer_detail, name='trainer_detail'), # Step 2: Detail view for a specific trainer
    path('students/', views.student_list, name='student_list'), # Step 1: List view for students
    path('students/<int:pk>/', views.student_detail, name='student_detail'), # Step 2: Detail view for a specific student
    
    # CRUD operation URLs for Course, Trainer, and Student
    # Create
    path('courses/add/', views.add_course, name='add_course'), # Step 3 : Add a new course
    path('trainers/add/', views.add_trainer, name='add_trainer'), # Step 3 : Add a new trainer
    path('students/add/', views.add_student, name='add_student'), # Step 3 : Add a new student
    # Update
    path('courses/<int:pk>/edit/', views.edit_course, name='edit_course'), # Step 4 : Edit an existing course
    path('trainers/<int:pk>/edit/', views.edit_trainer, name='edit_trainer'), # Step 4 : Edit an existing trainer
    path('students/<int:pk>/edit/', views.edit_student, name='edit_student'), # Step 4 : Edit an existing student
]