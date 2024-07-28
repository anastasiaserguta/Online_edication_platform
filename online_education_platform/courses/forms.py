from django import forms
from .models import Module

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class ModuleForm(forms.Form):
#     module_course = forms.CharField(disabled=True)
        

