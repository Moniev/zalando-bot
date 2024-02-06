from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request


def home(request: HttpRequest) -> HttpResponse:
    context: dict = {}
    return render(request, 'controller/home.html', context=context)

def about(request: HttpRequest) -> HttpResponse:
    context: dict = {}
    return render(request, 'controller/home.html', context=context)
