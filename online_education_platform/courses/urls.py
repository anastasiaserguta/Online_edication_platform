from django.urls import path
from . import views
from .views import CourseListView, CorseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, UserPostListView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-created-courses'),
    path('courses/<int:pk>/', CorseDetailView.as_view(), name='courses-detail'),
    path('courses/new/', CourseCreateView.as_view(), name='courses-create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
    path('', views.home, name='courses-home'),
    path('about/', views.about, name='courses-about'),
]

