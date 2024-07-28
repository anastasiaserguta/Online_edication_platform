from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.urls import reverse
from random import randint
from uuid import uuid4




# Модель курса, где title - название, description - описание, 
# teacher - преподаватель, который его создал, created - дата создания.
class Course(models.Model): 
    course_title = models.CharField(max_length=64, null=True, help_text='название курса')
    course_description = models.TextField(max_length=128, null=True, help_text='описание курса')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_creator')
    course_created = models.DateTimeField(auto_now_add=datetime)

    def __str__(self):
        return self.course_title
    
    def get_absolute_url(self):
        return reverse('courses-detail', kwargs={'pk': self.pk})
    
    


# Класс модулей, из которых состоит курс, 
# содержит объекты курса, название и описание.    
class Module(models.Model):
    module_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='module_course')
    module_title = models.CharField(max_length=200, null=False)
    module_description = models.TextField(blank=False, default='описание отсутствует')

    def __str__(self):
        return self.module_title
    
    def get_absolute_url(self):
        return reverse('module-detail', kwargs={'pk': self.pk})
    
    
class Task(models.Model):
    task_module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='task_module', default=None)
    task_title = models.CharField(max_length=128)
    task_description = models.TextField(blank=True)
    task_file = models.FileField(default=None)
    created_at = models.DateTimeField(auto_now_add=datetime)
    update_at = models.DateTimeField(auto_now=datetime)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title

    
class Solution(models.Model):
    solution_for_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='solution', default=None)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    email = models.EmailField(null=True)
    notes = models.IntegerField(null=True)
    solution_title = models.CharField(max_length=128)
    task_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=datetime)
    update_at = models.DateTimeField(auto_now=datetime)
    solution_description = models.TextField(blank=True)
    solution_code = models.UUIDField(unique=True)


    def __str__(self):
        return self.solution_title
    

class Student(models.Model):
    courses = models.ManyToManyField(Course)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_student')


    
        
    



