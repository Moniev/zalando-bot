from django import forms
from .models import User 
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class UserRegisterForm(UserCreationForm):
    email: forms.EmailField = forms.EmailField()
    username: forms.CharField = forms.CharField()
    password1: forms.CharField = forms.CharField()
    password2: forms.CharField = forms.CharField() 

    class Meta:
        model = User
        fields: list = ['username', 'email', 'password1', 'password2']

    def __repr__(self):
        return self

class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def formValid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Witaj {user}')
        return super().form_valid(form)
    
class MyLogoutView(LogoutView):
    template_name = 'users/logout.html' 

    def formValid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Witaj {user}')
        return super().form_valid(form)
    