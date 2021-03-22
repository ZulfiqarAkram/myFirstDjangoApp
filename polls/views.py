from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("you are looking detail of question %s" % question_id)


def results(request, question_id):
    return HttpResponse('you are looking results of question %s' % question_id)


def vote(request, question_id):
    return HttpResponse('you are voting on question %s' % question_id)
