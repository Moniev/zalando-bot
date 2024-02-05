from django.shortcuts import render
from django.http import HttpResponse, request
from .models import OpenDrop, UpcomingDrop

def home(request: request) -> HttpResponse:
    context: dict = {}
    return render(request, 'controller/home.html', context=context)

def about(request: request) -> HttpResponse:
    return render(request, 'controller/home.html')

