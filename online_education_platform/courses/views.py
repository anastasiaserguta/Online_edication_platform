from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from .models import Course, Module, Task, Solution, Student
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Module, Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


# courses = [
# 	{
#         'teacher': 'Админ',
#         'title': 'Курс русского языка (часть 1)',
#         'description': 'Описание курса.',
#         'date_posted': '24.07.2024'
# 	},
# 	{
#         'teacher': 'Пользователь',
#         'title': 'Курс русского языка (часть 2)',
#         'description': 'Описание курса.',
#         'date_posted': '25.07.2024'
# 	}
# ]

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
        solution = Solution.objects.filter(id=pk)
        context = {
                'tasks': Task.objects.filter(id=pk),
                'solution': solution,
        }
        return render(request, 'courses/task_detail.html', context)


class CourseCreateView(LoginRequiredMixin, CreateView):
        model = Course
        fields = ['course_title', 'course_description',]
        # permission_required = True


        def form_valid(self, form):
                form.instance.teacher = self.request.user
                return super().form_valid(form)
        
class TaskCreateView(LoginRequiredMixin, CreateView):
        model = Task

        fields = ['task_title', 'task_description', 'task_file', 'is_completed',]
        # permission_required = True

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
        
class ModuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Module
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


class UserPostListView(ListView):
	model = Course
	template_name = 'courses/user_created_courses.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'courses'
	paginate_by = 5

	def get_queryset(self):
                user = get_object_or_404(User, username=self.kwargs.get('username'))
                return Course.objects.filter(teacher=user).order_by('-course_created')





