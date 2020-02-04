from random import randint

from brain_games.cli import user_answer, ask_username

ROUNDS = 3


def random_number():
    number = randint(1, 100)
    return number


def welcome():
    name = ask_username()
    welcome = f'Hello, {name}!'
    return name
    print(welcome)


def run(game=None):
    print('Welcome to the Brain Games!')
    if game:
        print(game.WHAT_TO_DO)
    print()
    name = welcome()
    if game:
        print()
        functionality(name, game.what_question)


def functionality(name, play):
    how_much_correct_answer = 0
    while how_much_correct_answer < ROUNDS:
        question, correct_answer = play()
        print(question)
        answer = user_answer()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. 
            \tLet\'s try again, '{name}'!""")
        how_much_correct_answer += 1
    print(f'Congratulations, {name}!')
