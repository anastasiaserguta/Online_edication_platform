from typing import Any
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Course, Module, Task, Solution, Student
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course, Module, Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib import messages
from uuid import uuid4

def home(request):
        context = {
        'courses': Course.objects.all(),
	}
        return render(request, 'courses/home.html', context)

def about(request):
        return render(request, 'courses/about.html', {'title': 'About online platform.'})


class CourseListView(ListView):
        model = Course
        template_name = 'courses/home.html'  
        context_object_name = 'courses'
        ordering = ['-course_created']
        paginate_by = 5

def course_detail(request, pk):
        context = {
        'courses': Course.objects.filter(id=pk),
        'modules': Module.objects.filter(module_course_id=pk),
	}
        return render(request, 'courses/course_detail.html', context)

def subscribe_course(request, pk):
        try:
                stud = get_object_or_404(User, id=request.user.id)
                Student.objects.create(
                        person=stud,
                )
        except IntegrityError:
                try:
                        course = Course.objects.get(id=pk)
                        person = Student.objects.get(person_id=stud.id)
                        messages.info(request, 'Вы уже записаны на курс!')
                        return render(request, 'courses/subscribe_alert.html')
                except:
                        person.courses.add(course)
                        messages.success(request, 'Вы записались на курс!')
                        return render(request, 'courses/subscribe_alert.html')
        
                
        
def user_courses(request, pk):
        courses = Student.objects.get(person_id=request.user.id).courses.all()
        context = {
                'user_courses': courses,
        }
        return render(request, 'courses/user_courses.html', context)
        
        

def module_detail(request, pk):
        mod = Module.objects.filter(id=pk)
        for modul in mod:
                _id = modul.module_course_id
        context = {
                'courses': Course.objects.filter(id=_id),
                'modules': mod,
                'tasks': Task.objects.filter(task_module_id=pk)
        }
        return render(request, 'courses/module_detail.html', context)

def task_detail(request, pk):
        try:
                solution_user = Solution.objects.filter(student_id=request.user.id)
                solution = None
                for sol in solution_user:
                        if sol.solution_for_task_id == pk:
                                solution = sol
                                break      
        except Solution.DoesNotExist:
                solution = None
        context = {
                'tasks': Task.objects.filter(id=pk),
                'solution': solution,
        }
        return render(request, 'courses/task_detail.html', context)


class CourseCreateView(LoginRequiredMixin, CreateView):
        model = Course
        fields = ['course_title', 'course_description',]

        def form_valid(self, form):
                form.instance.teacher = self.request.user
                return super().form_valid(form)
        
        
class ModuleCreateView(LoginRequiredMixin, CreateView):
        model = Module
        fields = ['module_course', 'module_title', 'module_description',]

        def form_valid(self, form):
                form.instance.teacher = self.request.user
                return super().form_valid(form)
        
        def test_func(self):
                course = self.get_object()
                if self.request.user == course.teacher:
                        return True
                return False

class TaskCreateView(LoginRequiredMixin, CreateView):
        model = Task
        fields = ['task_module', 'task_title', 'task_description', 'task_file', 'is_completed',]


class SolutionCreateView(CreateView): # новое изменение
        model = Solution
        template_name = 'courses/solution_form.html'
        fields = ['solution_for_task', 'solution_title', 'solution_description', 'task_file',]

        def form_valid(self, form):
                form.instance.student = self.request.user
                form.instance.solution_code = uuid4()
                return super().form_valid(form)
        
class SolutionNotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Solution
        fields = ['notes', 'notation',]

        def test_func(self):
                return True

        
def solution_detail(request, pk):
        context = {
                'solution': get_object_or_404(Solution, id=pk),
        }
        return render(request, 'courses/solution_detail.html', context)


class ModuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Module
        success_url = '/'

        def test_func(self):
                return True

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Task
        success_url = '/'

        def test_func(self):
                return True        

class ModuleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Module
        fields = ['module_course', 'module_title', 'module_description',]

        def form_valid(self, form):
                return super().form_valid(form)

        def test_func(self):
                return True

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Course
        fields = ['course_title', 'course_description',]

        def form_valid(self, form):
                form.instance.teacher = self.request.user
                return super().form_valid(form)

        def test_func(self):
                course = self.get_object()
                if self.request.user == course.teacher:
                        return True
                return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Course
        success_url = '/'

        def test_func(self):
                cur_course = self.get_object()
                if self.request.user == cur_course.teacher:
                        return True
                return False


class UserCourseListView(ListView):
	model = Course
	template_name = 'courses/user_created_courses.html' 
	context_object_name = 'courses'
	paginate_by = 5

	def get_queryset(self):
                user = get_object_or_404(User, username=self.kwargs.get('username'))
                return Course.objects.filter(teacher=user).order_by('-course_created')
        






