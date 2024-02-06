from django.contrib.auth import views as auth_views
from django.urls import path
from users.forms import MyLoginView
import users.views as UsersViews
from . import views

urlpatterns: list = [
    path('', views.home, name='bome'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', UsersViews.loginUser, name='login'),
    path('logout', UsersViews.logoutUser, name='logout'),
    path('register', UsersViews.registerUser, name='register'),
    path('drops', UsersViews.drops, name='drops'),
]