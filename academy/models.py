from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    duration_in_weeks = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    course_image = models.ImageField(
        upload_to='course_images/',
        blank=True,
        null=True,
        default='images/default_course.png'
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
        default='images/default_profile.png'
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
    enrolled_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')
    enrollment_date = models.DateField()
    profile_picture = models.ImageField(
        upload_to='student_pictures/',
        blank=True,
        null=True,
        default='images/default_profile.png'
    )
    is_active = models.BooleanField(default=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
