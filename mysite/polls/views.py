#from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from django.forms.models import model_to_dict
from django.template import loader
import json
from .models import Question
from .models import Hackathon
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# Create your views here.

def detail(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def car(request):
    data = list(Hackathon.objects.values())
    return JsonResponse(data, safe=False)

# def info(request):
#     r = Hackathon.objects.order_by("distance").values_list("distance")[0:5]
#     dic = {'1':r[0],
#            '2':r[1],
#            '3':r[2],
#            '4':r[3],
#            '5':r[4]}
#     app_json = json.dumps(dic)
#     return HttpResponse(app_json)

