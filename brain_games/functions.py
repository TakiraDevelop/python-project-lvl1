from random import randint

from brain_games.cli import user_answer, ask_username

ROUNDS = 3


def random_number():
    number = randint(1, 100)
    return number


def welcome():
    name = ask_username()
    welcome = f'Hello, {name}!'
    print(welcome)
    return name


def run(game=None):
    print('Welcome to the Brain Games!')
    if game:
        print(game.WHAT_TO_DO)
    print()
    name = welcome()
    if game:
        print()
        game_runner(name, game.what_question)


def game_runner(name, play):
    how_much_rounds = 0
    how_much_correct_answers = 0
    while how_much_rounds < ROUNDS:
        question, correct_answer = play()
        print(question)
        answer = user_answer()
        if answer == correct_answer:
            print('Correct!')
            how_much_correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.", f"Let\'s try again, '{name}'!")
        how_much_rounds += 1
    if how_much_correct_answers == 3:
        print(f'Congratulations, {name}!')
