from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request
from django.contrib.auth.decorators import login_required
from controller.models import OpenDrop, UpcomingDrop
from .bot.main import executeNow


def home(request: HttpRequest) -> HttpResponse:
    context: dict = {}
    return render(request, 'controller/home.html', context=context)

def about(request: HttpRequest) -> HttpResponse:
    context: dict = {}
    return render(request, 'controller/home.html', context=context)

@login_required
def botManual(request: HttpRequest) -> HttpResponse:
    context: dict = {}             
    return render(request, 'controller/bot_manual.html', context=context)

@login_required
def loginBot(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        executeNow()

@login_required
def logoutBot(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        executeNow()

@login_required
def checkOpenDrops(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        executeNow()

@login_required
def checkUpcomingDrops(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        executeNow()

def drops(request: HttpRequest) -> HttpResponse:
    open_drops = OpenDrop.objects.all()
    upcoming_drops = UpcomingDrop.objects.all()

    context: dict = {'open_drops': open_drops, 'upcoming_drops': upcoming_drops}
    
    return render(request, 'users/drops.html', context)

