import prompt
from brain_games.functions import welcome, run, question


def user_name():
    name = prompt.string('May I have your name? ')
    return name


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def task(game):
    if game == 'calc':
        print('What is the result of the expression?')
    elif game == 'even':
        print('Answer "yes" if number even otherwise answer "no".')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == 'progression':
        print('What number is missing in the progression?')


def package_game(game):
    welcome()
    task(game)
    name = user_name()
    run(name)
    question(name, game)

