from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .models import WebsiteLoginInfo, WebsiteLogoutInfo
from django.contrib.auth.views import LoginView, LogoutView

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields: list = ['username', 'email', 'password1', 'password2']


class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def formValid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Welcome {user}')
        return super().form_valid(form)
    
class MyLogoutView(LogoutView):
    template_name = 'users/logout.html' 

    def formValid(self):
        pass