from django.contrib import admin
from .models import Course, Module, Task, Solution, Student


class ModuleInline(admin.StackedInline):
    model = Module

class TaskInline(admin.StackedInline):
    model = Task

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'teacher',]
    list_filter = []
    prepopulated_fields = {'course_title': ('course_description',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_title', 'module_description',]
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_title', 'task_description', 'created_at', 'is_completed',]

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['solution_title', 'student', 'email', 'solution_description', 'created_at', 'update_at', 'task_file', 'solution_code', 'notes',]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['person',]




    

