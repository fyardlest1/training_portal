from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    duration_in_weeks = models.IntegerField()
    course_image = models.ImageField(
        upload_to='course_images/',
        blank=True,
        null=True,
        default='course_images/default.jpg'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
    

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=100)
    profile_picture = models.ImageField(
        upload_to='instructor_pictures/',
        blank=True,
        null=True,
        default='instructor_pictures/default_profile.png'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    profile_picture = models.ImageField(
        upload_to='student_pictures/',
        blank=True,
        null=True,
        default='student_pictures/default_profile.png'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"