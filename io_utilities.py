
def read_answer():
    answer = input('answer: ')
    return answer

def print_question(question):
    print(question['question'])
    for i in question['answers']:
        print(i)

def setup_quiz():
    print('Welcome to the random exam generator!')
    difficulty = input('''How difficult would you like this quiz to be? 
1: easy
2: medium
3: hard
4: any
difficulty: ''')
    while difficulty.strip() not in ['easy','medium','hard', 'any']:
        difficulty = input('''Invalid option, the options are:
1: easy
2: medium
3: hard
4: any
difficulty: ''')
    number_of_questions = input('How many questions would you like to answer? ')
    print('Let the games begin!')
    return {'difficulty' : difficulty, 'number_of_questions': number_of_questions}

def play_again():
    answer = ''
    again = input('''Thank you for playing, would you like to play again?[yes/no]
''')
    while True:
        if again not in ['yes','no']:
            again = input('''Invalid input, would you like to play again?[yes/no]
''')
        else:
            break
    if again == 'yes':
        return True
    else:
        return False

def ask_question(question):
    print(question['question'])
    for i,j in enumerate(question['answers']):
        print(str(i) + ': ' + j)
    ans = input('answer: ')
    if ans == question['correct answer']:
        return 1
    else:
        return 0
    
def print_score(correct, total):
    print('You scored ' + correct + ' out of ' + total + ' points.')
