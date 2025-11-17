from django.contrib import admin
from .models import Course, Trainer, Student

# Register your models here.
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Student)