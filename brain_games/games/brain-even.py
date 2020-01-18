from brain_games.functions import rnumber

WHAT_TO_DO = 'Answer "yes" if number even otherwise answer "no".'


def what_question():
    number = rnumber()
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    return 'no' if number % 2 else 'yes'