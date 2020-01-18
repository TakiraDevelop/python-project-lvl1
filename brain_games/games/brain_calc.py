import operator
from random import choice

from brain_games.functions import rnumber

WHAT_TO_DO = 'What is the result of the expression?'


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def what_operation():
    return choice(list(operations.keys()))


def correct_answer(num1, operation, num2):
    return str(operations[operation](num1, num2))


def what_question():
    num1 = rnumber()
    num2 = rnumber()
    operation = what_operation()
    question = f'Question: {num1} {operation} {num2}'
    answer = correct_answer(num1, operation, num2)
    return (question, answer)
