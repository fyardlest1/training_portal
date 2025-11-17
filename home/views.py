from django.shortcuts import render

from academy.models import Course, Trainer, Student


# Create your views here.
def index(request):
    courses = Course.objects.all().count()
    instructors = Trainer.objects.all().count()
    students = Student.objects.all().count()
    
    context = {
        'courses': courses,
        'instructors': instructors,
        'students': students,
    }
    return render(request, 'home/index.html', context)
