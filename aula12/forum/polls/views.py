from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("O Mário é um cara legal.")
