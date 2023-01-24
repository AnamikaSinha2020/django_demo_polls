from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<http>Hello World!! you are at poll index.</http>")

# Create your views here.
def details(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voteing on question %s." %question_id)



