from django import forms
from .models import Course, Trainer, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'duration_in_weeks', 'price', 'course_image']
        # Bootstrap 5 requires adding the class to the underlying widget
        # Instead of template filters, the cleanest / safest way is to add the class directly in the form:
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duration_in_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
        
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'email', 'expertise', 'profile_picture', 'bio', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'expertise': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'enrolled_course', 'enrollment_date', 'profile_picture', 'is_active', 'trainer']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enrolled_course': forms.Select(attrs={'class': 'form-control'}),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
        }