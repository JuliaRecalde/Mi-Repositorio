from django.shortcuts import render

from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question


from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "reserva/index.html", context)


