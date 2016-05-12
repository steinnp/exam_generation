
def generate_data():
    questions = []
    q1 = {'response': 0, 'category': 'animals', 'difficulty': 'medium',
          'question': 'How many animals?', 'correct answer': 'yes',
          'answers': ['yes','no','maybe','maybe not']}
    questions.append(q1)
    q2 = {'response': 0, 'category': 'books', 'difficulty': 'hard',
          'question': 'How many books?', 'correct answer': 'no',
          'answers': ['yes','no','really','maybe not']}
    questions.append(q2)
    q3 = {'response': 0, 'category': 'sports', 'difficulty': 'medium',
          'question': 'How many sports?', 'correct answer': 'football',
          'answers': ['football','no','maybe','maybe not']}
    questions.append(q3)
    q4 = {'response': 0, 'category': 'science', 'difficulty': 'medium',
          'question': 'How many science?', 'correct answer': 'Stephen Hawking',
          'answers': ['yes','no','Stephen Hawking','maybe not']}
    questions.append(q4)
    return questions
