from django.shortcuts import render
from django.http import HttpResponse, request


def home(request: request) -> HttpResponse:
    context: dict = {}
    return render(request, 'backend/home.html', context=context)

def about(request: request) -> HttpResponse:
    return render(request, 'backend/home.html')



# Create your views here.
