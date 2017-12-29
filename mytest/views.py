# -*- coding:utf-8 –*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice


def index(request):
    return HttpResponse('xiaoyan')


def detail(request, question_id):
    return HttpResponse('你正在看问题 s%.', question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index_01(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def detail_01(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def detail_02(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def detail_03(request):
    question = Question.objects.all()
    return render(request, 'detail.html', {'question': question})


def detail_04(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'detail_04.html', {'question': question})
