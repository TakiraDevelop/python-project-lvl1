import operator
from random import choice

from brain_games.functions import random_number

WHAT_TO_DO = 'What is the result of the expression?'


OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul)
)


def what_question():
    num1 = random_number()
    num2 = random_number()
    symbol, operation = choice(OPERATIONS)
    question = f'Question: {num1} {symbol} {num2}'
    answer = operation(num1, num2)
    return (str(question), str(answer))
