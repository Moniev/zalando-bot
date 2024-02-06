from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from controller.models import OpenDrop, UpcomingDrop
from users.models import WebsiteLoginInfo, WebsiteLogoutInfo
from .forms import UserRegisterForm


def registerUser(request: HttpRequest) -> HttpResponse:    
    if request.method == "POST":
        form: UserRegisterForm = UserRegisterForm(request.POST)
        if form.is_valid():
            username: str = form.cleaned_data.get('username')
            email: str = form.cleaned_data.get('email')
            if len(User.objects.filter(email=email)) == 0:
                form.save()
            else:
                messages.error(request, f'Nie udało się Ci się założyć konta!')
                return redirect('register')
            messages.success(request, f'Udało Ci się stworzyć konto, {username}!')
            return redirect('login')
        else:
            messages.error(request, f'Nie udało się Ci się założyć konta!')
            print(form.errors.as_data())
    else:
        form: UserRegisterForm = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def loginUser(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username: str = request.POST.get('username')
        password: str = request.POST.get('password')
        user: User = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Udało się Ci się zalogować {username}!')
            login_info: WebsiteLogoutInfo = WebsiteLogoutInfo(user_id=user.id)
            login_info.save()
            return redirect('home')
        else:
            messages.error(request, f'Nie udało się Ci się zalogować!')
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

def logoutUser(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        logout_info: WebsiteLogoutInfo = WebsiteLogoutInfo()
        logout_info.save()
        logout(request=request)
        messages.success(request, 'Zostałeś wylogowany!')
        return redirect('login')
    if request.method == "GET":
        return render(request, 'users/logout.html')

def drops(request: HttpRequest) -> HttpResponse:
    open_drops = OpenDrop.objects.all()
    upcoming_drops = UpcomingDrop.objects.all()

    context: dict = {'open_drops': open_drops, 'upcoming_drops': upcoming_drops}
    
    return render(request, 'users/drops.html', context)
    
