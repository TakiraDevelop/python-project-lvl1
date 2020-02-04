from brain_games.functions import random_number

WHAT_TO_DO = 'Find the greatest common divisor of given numbers.'


def what_question():
    num1 = random_number()
    num2 = random_number()
    question = f'Question: {num1} {num2}'
    answer = gcd(num1, num2)
    return (question, str(answer))


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)