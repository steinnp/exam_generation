from django.shortcuts import render
#from . import api_utilities
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('polls/index.html') 
    return HttpResponse(template.render())
