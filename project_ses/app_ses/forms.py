from django import forms
from .models import AppUser, Student, Course

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("full name","email","password","usertype","contact")
        model = AppUser 

class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("email","password")
        #fields = "_all_" - incase of all fields   
        model = AppUser 

class CourseCreateForm(forms.ModelForm):
    class Meta:
        fields = ("title","code")
        model = Course 

class StudentCreateForm(forms.ModelForm):
    class Meta:
        fields = ("first name","middle_name","last_name","email","contact","gender","blood_group","academic_level","academic_status","academic_org","academic_score","course","intake","shift","remarks")
        model = Student 
        
