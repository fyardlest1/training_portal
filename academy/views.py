from django.shortcuts import render, get_object_or_404, redirect

from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm, StudentForm



# reate views for Course, Trainer, and Student
def course_list(request): # Step 1: Logic to retrieve and display a list of courses
    # Logic to retrieve and display a list of courses
    courses = Course.objects.all()
    
    context = {
        'courses': courses,
    }
    return render(request, 'academy/course-list.html', context)


def course_detail(request, pk): # Step 2: Detail view for a specific course
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


def add_course(request): # Step 3: Logic to add a new course
    # Logic to add a new course
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            # Redirect to course list or detail page after saving
            return redirect('course_list')
    else:
        course_form = CourseForm()
        
    context = {
        'course_form': course_form,
    }
    return render(request, 'academy/add-course.html', context)


def trainer_list(request): # Step 1: Logic to retrieve and display a list of trainers
    # Logic to retrieve and display a list of trainers
    instructors = Trainer.objects.all()
    
    context = {
        'instructors': instructors
    }
    return render(request, 'academy/trainer-list.html', context)


def trainer_detail(request, pk): # Step 2: Detail view for a specific trainer
    # Logic to retrieve and display details of a specific trainer
    try:
        trainer = get_object_or_404(Trainer, pk=pk)
    except Trainer.DoesNotExist:
        trainer = None
        
    context = {
        'trainer': trainer,
    }
    return render(request, 'academy/trainer-detail.html', context)


def add_trainer(request): # Step 3: Logic to add a new trainer
    # Logic to add a new trainer
    if request.method == 'POST':
        trainer_form = TrainerForm(request.POST, request.FILES)
        if trainer_form.is_valid():
            trainer_form.save()
            # Redirect to trainer list or detail page after saving
            return redirect('trainer_list')
    else:
        trainer_form = TrainerForm()
        
    context = {
        'trainer_form': trainer_form,
    }
    return render(request, 'academy/add-trainer.html', context)


def student_list(request): # Step 1: Logic to retrieve and display a list of students
    # Logic to retrieve and display a list of students
    students = Student.objects.all()
    # trainer = Trainer.objects.get_queryset()
        
    context = {
        'students': students,
        # 'trainer': trainer,
    }
    return render(request, 'academy/student-list.html', context)


def student_detail(request, pk): # Step 2: Detail view for a specific student
    # Logic to retrieve and display details of a specific student
    try:
        student = get_object_or_404(Student, pk=pk)
    except Student.DoesNotExist:
        student = None
        
    context = {
        'student': student,
    }
    return render(request, 'academy/student-detail.html', context)


def add_student(request): # Step 3: Logic to add a new student
    # Logic to add a new student
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            # Redirect to student list or detail page after saving
            return redirect('student_list')
    else:
        student_form = StudentForm()
        
    context = {
        'student_form': student_form,
    }
    return render(request, 'academy/add-student.html', context)