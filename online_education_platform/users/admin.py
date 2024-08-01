from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image',]

