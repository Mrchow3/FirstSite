from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def polling(request):
    latest_questions = Question.objects.order_by('date')[:5]
    context = {"Question": Question.objects.all, "Choice":Choice.objects.all,"latest_questions" : latest_questions}

    return render(
        request = request,
        template_name = "polls/index.html",
        context = context)

def detail(request,question_id):
    return HttpResponse(f"Question #{question_id}")

def results(request, question_id):
    return HttpResponse(f"Here are the results of question #{question_id}") 

def vote(requests, question_id):
    return HttpResponse(f"Voting on question #{question_id}")

       