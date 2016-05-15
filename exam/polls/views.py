from django.shortcuts import render
from .api_utilities import get_questions, get_session_token
from django.template import loader
from django.http import HttpResponse
from .forms import QuestionSettingsForm, QuestionForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    template = loader.get_template('polls/index2.html') 
    if request.method == 'POST':
        form = QuestionSettingsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'polls/index2.html', {'form': form})
    else:
        form = QuestionSettingsForm()
    return render(request, 'polls/index2.html', {'form': form})

def questions(request):
    template = loader.get_template('polls/name.html')
    question_list = get_questions(request.POST['number_of_questions'],request.POST['difficulty'], None)
    
    form = QuestionForm(request.POST or None, extra=question_list)
    return render(request, 'polls/name.html', {'form': form})
