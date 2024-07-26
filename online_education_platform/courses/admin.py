from django.contrib import admin
from .models import Course, Module, Task


class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'teacher',]
    list_filter = []
    prepopulated_fields = {'course_title': ('course_description',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_title', ]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_title', 'created_at', 'is_completed',]




    

