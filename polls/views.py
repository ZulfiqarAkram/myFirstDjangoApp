from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello world! you are index of polls app")


def detail(request, question_id):
    return HttpResponse('you are looking at question %s' % question_id)


def results(request, question_id):
    return HttpResponse('you are looking results of question %s' % question_id)


def vote(request, question_id):
    return HttpResponse('you are voting on question %s' % question_id)
