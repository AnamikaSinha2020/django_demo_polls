from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<http>Hello World!! you are at poll index.</http>")

# Create your views here.
