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
    code_course = str(randint(99999999999999999999, 99999999999999999999999))
    save_code = models.CharField(max_length=30, default=code_course, editable=False)
    # enter_code_course = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.course_title
    
    def get_absolute_url(self):
        return reverse('courses-detail', kwargs={'pk': self.pk})

# Класс модулей, из которых состоит курс, 
# содержит объекты курса, название и описание.    
class Module(models.Model):
    module_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='module_course', default=None)
    in_course = models.CharField(max_length=30, default=Course.code_course)
    module_title = models.CharField(max_length=200, null=True)
    module_description = models.TextField(blank=True)
    code_module = str(randint(99999999999999999999, 99999999999999999999999))
    # enter_code_modules = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.module_title
    
    
class Task(models.Model):
    task_module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='task_module', default=None)
    in_module = models.CharField(max_length=30, default=Module.code_module)
    task_title = models.CharField(max_length=128)
    task_description = models.TextField(blank=True)
    task_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=datetime)
    update_at = models.DateTimeField(auto_now=datetime)
    is_completed = models.BooleanField(default=False)
    code_task = str(randint(99999999999999999999, 99999999999999999999999))

    def __str__(self):
        return self.task_title

    
class Solution(models.Model):
    solution_for_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='solution', default=None)
    for_task = models.CharField(max_length=30, default=Task.code_task)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    email = models.EmailField(null=True)
    notes = models.IntegerField(null=True)
    solution_title = models.CharField(max_length=128)
    task_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=datetime)
    update_at = models.DateTimeField(auto_now=datetime)
    solution_description = models.TextField(blank=True)
    solution_code = models.CharField(max_length=30, default=str(randint(99999999999999999999, 99999999999999999999999)))

    def __str__(self):
        return self.solution_title


    
        
    



