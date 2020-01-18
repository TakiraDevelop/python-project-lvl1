from random import choice, randint

WHAT_TO_DO = 'What number is missing in the progression?'


def progression():
    number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    max_number = (delta * length) + number
    prog = range(number, max_number, delta)
    return prog


def what_question():
    prog == progression()
    fnumber = choice(prog)
    progression = ' '.join([
        '..' if num == fnumber else str(num) for num in prog
    ])
    question = f'Question: {progression}'
    return (question, str(fnumber))
