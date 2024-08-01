from django import forms
from django.forms import ModelForm
from .models import Task, Student

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.Form):
    class Meta: 
        model = Student
        fields = ['courses', ]

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task_module', 'task_title', 'task_description', 'task_file', 'is_completed',)







