from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image',]

admin.site.unregister(Group)

# @admin.register(TeachersGroup)
# class TeachersGroupAdmin(GroupAdmin):
#     fieldsets = ((None, {'fields': ('group_name', 'permissions')}), (('Description'), {'fields': ('teachers_description',)}),)

# @admin.register(StudentsGroup)
# class StudentsCroupAdmin(GroupAdmin):
#     fieldsets = ((None, {'fields': ('group_name', 'permissions')}), (('Description'), {'fields': ('students_description',)}),)