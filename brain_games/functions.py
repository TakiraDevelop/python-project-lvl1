from random import randint

from brain_games.cli import user_answer, user_name

ROUNDS = 3


def rnumber():
    number = randint(1, 100)
    return number


def welcome():
    name = user_name()
    welcome = f'Hello, {name}!'
    print(welcome)


def is_answer_correct(answer, correct_answer):
    if answer == correct_answer:
        message = 'Correct!'
        return (message)
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (message.format(wrong = answer, correct = correct_answer))


def run(game = None):
    print('Welcome to the Brain Games!')
    if game:
        print(game.WHAT_TO_DO)
    print()
    name = welcome()
    if game:
        print()
        functionality(name, game.what_question)


def functionality(name, play)
    correct_answer = 0
    while correct_answer < ROUNDS:
        question, correct_answer = play()
        print(question)
        res, msg = is_answer_correct(user_name(), correct_answer)
        print(msg)
        if not res:
            print(f'Let\'s try again, {name}!')
            return
        correct_answer += 1
    print(f'Congratulations, {name}!')