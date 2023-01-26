
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=', '.join([q.question_text for q in latest_question_list] )
   # template = loader.get_template('polls/index.html')
    #context = {
     #   'latest_question_list': latest_question_list,
    #}
    context={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

# Create your views here.
def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exits")
    return render(request, ' polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):


    response = "You're looking at results of question %s."

    return HttpResponse("You are result on question %s." %question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." %question_id)



