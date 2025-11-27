from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

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


@login_required
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


@login_required
@permission_required('academy.add_course', raise_exception=True)
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


@login_required
@permission_required('academy.change_course', raise_exception=True)
def edit_course(request, pk=None): # Step 4: Logic to edit an existing course
    # Logic to edit an existing course
    course = get_object_or_404(Course, pk=pk) # get the course object
    
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES, instance=course)
        if course_form.is_valid():
            course_form.save()
            # Redirect to course detail page after saving where pk is course.pk
            return redirect('course_detail', pk=course.pk) 
    else:
        course_form = CourseForm(instance=course)
        
    context = {
        'course_form': course_form, # form instance to be used in the template
        'course': course, # course instance to be used in the template
    }
    return render(request, 'academy/edit-course.html', context)


@login_required
@permission_required('academy.delete_course', raise_exception=True)
def delete_course(request, pk): # Step 5: Logic to delete an existing course
    # Logic to delete an existing course
    course = get_object_or_404(Course, pk=pk) # get the course object
    
    course.delete()
    return redirect('course_list')


def trainer_list(request): # Step 1: Logic to retrieve and display a list of trainers
    # Logic to retrieve and display a list of trainers
    instructors = Trainer.objects.all()
    
    context = {
        'instructors': instructors
    }
    return render(request, 'academy/trainer-list.html', context)


@login_required
def trainer_detail(request, pk=None): # Step 2: Detail view for a specific trainer
    # Logic to retrieve and display details of a specific trainer
    try:
        trainer = get_object_or_404(Trainer, pk=pk)
    except Trainer.DoesNotExist:
        trainer = None
        
    context = {
        'trainer': trainer,
    }
    return render(request, 'academy/trainer-detail.html', context)


@login_required
@permission_required('academy.add_trainer', raise_exception=True)
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


@login_required
@permission_required('academy.change_trainer', raise_exception=True)
def edit_trainer(request, pk=None): # Step 4: Logic to edit an existing trainer
    # Logic to edit an existing trainer
    trainer = get_object_or_404(Trainer, pk=pk) # get the trainer object
    
    if request.method == 'POST':
        trainer_form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if trainer_form.is_valid():
            trainer_form.save()
            # Redirect to trainer detail page after saving where pk is trainer.pk
            return redirect('trainer_detail', pk=trainer.pk) 
    else:
        trainer_form = TrainerForm(instance=trainer)
        
    context = {
        'trainer_form': trainer_form, # form instance to be used in the template
        'trainer': trainer, # trainer instance to be used in the template
    }
    return render(request, 'academy/edit-trainer.html', context)


@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def delete_trainer(request, pk): # Step 5: Logic to delete an existing trainer
    # Logic to delete an existing trainer
    trainer = get_object_or_404(Trainer, pk=pk) # get the trainer object
    
    trainer.delete()
    return redirect('trainer_list')


def student_list(request): # Step 1: Logic to retrieve and display a list of students
    # Logic to retrieve and display a list of students
    
    # get the logged-in user
    # user = request.user
    
    # get the list of students
    students = Student.objects.all().order_by('last_name')
    paginator = Paginator(students, 10)  # Show 10 students per page
    
    # Get the page number from request GET parameters
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # Auto-handles invalid input
        
    # trainer = Trainer.objects.get_queryset()
        
    context = {
        'students': students,
        'page_obj': page_obj,
    }
    return render(request, 'academy/student-list.html', context)


@login_required
def student_detail(request, pk=None): # Step 2: Detail view for a specific student
    # Logic to retrieve and display details of a specific student
    try:
        student = get_object_or_404(Student, pk=pk)
    except Student.DoesNotExist:
        student = None
        
    context = {
        'student': student,
    }
    return render(request, 'academy/student-detail.html', context)


@login_required
@permission_required('academy.add_student', raise_exception=True)
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


@login_required
@permission_required('academy.change_student', raise_exception=True)
def edit_student(request, pk=None): # Step 4: Logic to edit an existing student
    # Logic to edit an existing student
    student = get_object_or_404(Student, pk=pk) # get the student object
    
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student_form.save()
            # Redirect to student detail page after saving where pk is student.pk
            return redirect('student_detail', pk=student.pk) 
    else:
        student_form = StudentForm(instance=student)
        
    context = {
        'student_form': student_form, # form instance to be used in the template
        'student': student, # student instance to be used in the template
    }
    return render(request, 'academy/edit-student.html', context)


@login_required
@permission_required('academy.delete_student', raise_exception=True)
def delete_student(request, pk): # Step 5: Logic to delete an existing student
    # Logic to delete an existing student
    student = get_object_or_404(Student, pk=pk) # get the student object
    
    student.delete()
    return redirect('student_list')
