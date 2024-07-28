from django.urls import path
from django.conf.urls import static
from .views import (CourseListView, 
                    # CourseDetailView, 
                    CourseCreateView, 
                    CourseUpdateView, 
                    CourseDeleteView, 
                    UserPostListView, 
                    # ModuleListView,
                    # ModuleDetailView,
                    ModuleCreateView,
                    home,
                    about,
                    course_detail,
                    module_detail,
                    task_detail,
                    ModuleDeleteView,
                    ModuleUpdateView,
                    TaskCreateView)
                    

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-created-courses'),
    path('courses/<int:pk>/', course_detail, name='courses-detail'),
    path('courses/new/', CourseCreateView.as_view(), name='courses-create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
    path('module/<int:pk>/', module_detail, name='module-detail'),
    path('module/<int:pk>/update/', ModuleUpdateView.as_view(), name='update-module'),
    path('module/<int:pk>/new/', ModuleCreateView.as_view(), name='create-module'),
    path('module/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module-delete'),
    path('task/<int:pk>/', task_detail, name='task-detail'),
    path('task/<int:pk>/new/', TaskCreateView.as_view(), name='create-task'),
    path('', home, name='courses-home'),
    path('about/', about, name='courses-about'),
] 

