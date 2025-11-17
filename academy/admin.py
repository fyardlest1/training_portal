from django.contrib import admin
from .models import Course, Trainer, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration_in_weeks', 'created_at')
    list_filter = ('created_at', 'duration_in_weeks')
    search_fields = ('course_name',)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'expertise', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at',)
    list_editable = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email', 'expertise')
    ordering = ('last_name', 'first_name')
    list_display_links = ('full_name', 'email')
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'enrolled_course', 'enrollment_date', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',) 
    search_fields = ('first_name', 'last_name', 'email')   
    ordering = ('last_name', 'first_name')
    list_display_links = ('full_name', 'email')


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)