from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Course, Module, Task
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Module, Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})


class CourseListView(ListView):
        model = Course
        template_name = 'courses/home.html'  
        context_object_name = 'courses'
        ordering = ['-course_created']
        paginate_by = 5


class CorseDetailView(DetailView):
        model = Course


class CourseCreateView(LoginRequiredMixin, CreateView):
        model = Course
        fields = ['course_title', 'course_description',]

        def form_valid(self, form):
                form.instance.teacher = self.request.user
                return super().form_valid(form)


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





