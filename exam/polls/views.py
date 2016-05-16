from django.shortcuts import render
from .api_utilities import get_questions, get_session_token
from django.template import loader
from django.http import HttpResponse
from .forms import QuestionSettingsForm, QuestionForm

# ask the user how many questions and of what difficulty he would like to be asked
def index(request):
    # initialize a session token for the user if it does not exist 
    #to make sure he never gets the same
    # question twice
    if 'session token' not in request.session:
        request.session['session token'] = get_session_token()
    if request.method == 'POST':
        form = QuestionSettingsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'polls/index2.html', {'form': form})
    else:
        form = QuestionSettingsForm()
    return render(request, 'polls/index2.html', {'form': form})

# Ask the user the questions he would like to answer
def questions(request):
    # initialize a session token for the user if it does not exist 
    # to make sure he never gets the same
    # question twice
    if 'session token' not in request.session:
        request.session['session token'] = get_session_token()
    # get a list of questions from an online api
    question_list = get_questions(request.POST['number_of_questions'],request.POST['difficulty'], request.session['session token'])
    form = []
    # display relevant data to the user
    for i in question_list:
        request.session[i['correct answer']] = i['correct answer']
        form.append((i['question'], i['answers']))
    # set the total number of questions the user will be asked in the session dict
    request.session['total questions'] = request.POST['number_of_questions']
    return render(request, 'polls/name.html', {'form': form})

# displays how well the user did in the quiz he just took
def answers(request):
    total = 0
    if 'total questions' in request.session:
        total = request.session['total questions']
    correct = 0
    for key in request.POST:
        if request.POST[key] in request.session:
            correct += 1
    if 'all_answers' not in request.session:
        request.session['all_answers'] = total
    else:
        request.session['all_answers'] = int(request.session['all_answers']) + int(total)
    if 'total_correct' not in request.session:
        request.session['total_correct'] = correct
    else:
        request.session['total_correct'] = int(request.session['total_correct']) + int(correct)
    return render(request, 'polls/answers.html',{
                  'correct': str(correct), 
                  'total': str(total), 'form': request.POST, 
                  'total_correct': request.session['total_correct'], 
                  'all_answers': request.session['all_answers']})
