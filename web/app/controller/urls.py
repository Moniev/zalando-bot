from django.urls import path
import users.views as UsersViews
from . import views

urlpatterns: list = [
    path('', views.home, name='bome'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', UsersViews.loginUser, name='login'),
    path('logout', UsersViews.logoutUser, name='logout'),
    path('register', UsersViews.registerUser, name='register'),
    path('profile', UsersViews.registerUser, name='profile'),
    path('drops', views.drops, name='drops'),
    path('manual', views.botManual, name='bot-manual'),
    path('shots', views.botManual, name='shot-story'),
    path('loginBot', views.loginBot, name='login-bot'),
    path('logoutBot', views.logoutBot, name='logout-bot'),
    path('checkOpenDropsBot', views.checkOpenDrops, name='check-open-drops-bot'),
    path('checkUpcomingDropsBot', views.checkUpcomingDrops, name='check-upcoming-drops-bot'),
]