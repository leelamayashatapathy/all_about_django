from django import forms
from .models import Student


#Django normal form
# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     age = forms.IntegerField()
#     phone = forms.CharField(max_length=12)
    
#Model form



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone', 'email', 'gender', 'age', 'dob', 'file', 'profile_image', 'bio']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'file': forms.ClearableFileInput(attrs={'multiple': False}),
            'profile_image': forms.ClearableFileInput(attrs={'multiple': False}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
