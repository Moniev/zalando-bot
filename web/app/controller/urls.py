from django.contrib.auth import views as auth_views
from django.urls import path
from users.forms import MyLoginView
import users.views as user_views
from . import views

urlpatterns: list = [
    path('', views.home, name='bome'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', MyLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register', user_views.register, name='register'),
]