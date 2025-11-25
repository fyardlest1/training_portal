from django.shortcuts import render, get_object_or_404
from .models import Course, Trainer, Student



def course_list(request):
    # Logic to retrieve and display a list of courses
    courses = Course.objects.all()
    
    context = {
        'courses': courses,
    }
    return render(request, 'academy/course-list.html', context)


def course_detail(request, pk):
    # Logic to retrieve and display details of a specific course
    try:
        # get 0 or more records from the database
        course = get_object_or_404(Course, pk=pk)        
    except Course.DoesNotExist: # if no record found
        course = None # assign None to course variable
        
    context = {
            'course': course,
        }
    return render(request, 'academy/course-detail.html', context)


def trainer_list(request):
    # Logic to retrieve and display a list of trainers
    instructors = Trainer.objects.all()
    
    context = {
        'instructors': instructors
    }
    return render(request, 'academy/trainer-list.html', context)


def trainer_detail(request, pk):
    # Logic to retrieve and display details of a specific trainer
    pass


def student_list(request):
    # Logic to retrieve and display a list of students
    students = Student.objects.all()
    # trainer = Trainer.objects.get_queryset()
        
    context = {
        'students': students,
        # 'trainer': trainer,
    }
    return render(request, 'academy/student-list.html', context)


def student_detail(request, pk):
    # Logic to retrieve and display details of a specific student
    pass
