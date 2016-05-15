import io_utilities
import mock_data
import api_utilities

def play():
    #session_token = api_utilities.get_session_token()
    session_token = None
    main(session_token)
    while True:
        if io_utilities.play_again():
            main(session_token)
        else:
            break

def main(session_token):
    settings = io_utilities.setup_quiz()
    num_questions = settings['number_of_questions']
    difficulty = settings['difficulty']

    questions = api_utilities.get_questions(num_questions, difficulty, session_token)
    correct_answers = 0
    for i in questions:
       correct_answers += io_utilities.ask_question(i)
    io_utilities.print_score(str(correct_answers), num_questions)

    






play()
