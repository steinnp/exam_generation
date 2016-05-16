import urllib.request
import json


#There might be some problems with unicode strings vs. ascii strings here
#polls the api for random questions and returns a list of question dictionaries
def get_questions(num_questions, difficulty, token = None):
    http_link = 'http://www.opentdb.com/api.php?amount=' + str(num_questions)
    http_link += '&type=multiple'
    if difficulty != 'any':
        http_link += '&difficulty=' + difficulty
    if token != None:
        http_link += '&token=' + token
    request = json.loads(urllib.request.urlopen(http_link).read().decode('utf-8'))
    if request['response_code'] != 0:
        return None
    request = request['results']
    questions = []
    for i in request:
        question = dict()
        question['question'] = i['question']
        question['category'] = i['category']
        question['correct answer'] = i['correct_answer']
        answers = i['incorrect_answers']
        answers.append(i['correct_answer'])
        question['answers'] = answers
        questions.append(question)
    return questions
        

#print(get_questions('3','medium', 'dec3fd8ba5801acf0bd8088478918c310f068fce867d293f6f14fcc687b43a1a'))

# gets a session token for the user to ensure he does not get the same question twice
# in one session
def get_session_token():
    http_link = 'http://www.opentdb.com/api_token.php?command=request'
    token = json.loads(urllib.request.urlopen(http_link).read().decode())
    return token['token']
    

print(get_questions("5", "easy"))
