import io_utilities
import mock_data

def play():
    main()
    while True:
        if io_utilities.play_again():
            main()
        else:
            break

def main():
    settings = io_utilities.setup_quiz()
    num_questions = settings['number_of_questions']
    difficulty = settings['difficulty']
    #request data from the api here
    #below is the mock data returned
    questions = mock_data.generate_data()
    print(questions)
    correct_answers = 0
    for i in questions:
       correct_answers += io_utilities.ask_question(i)
    io_utilities.print_score(str(correct_answers), num_questions)

    






play()
