from django.urls import path, include
from . import views


urlpatterns: list = [path('', views.home, name='home'), path('about', views.about, name='about')]