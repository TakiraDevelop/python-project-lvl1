from brain_games.functions import random_number

WHAT_TO_DO = 'Answer "yes" if number even otherwise answer "no".'


def what_question():
    number = random_number()
    question = f'Question: {number}'
    if number % 2:
        answer = 'no'
    else:
        answer = 'yes'
    return (question, answer)
    