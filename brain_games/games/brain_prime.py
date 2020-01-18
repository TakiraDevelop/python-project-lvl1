from brain_games.functions import rnumber

WHAT_TO_DO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    prime_number = 2
    while number % prime_number != 0:
        prime_number += 1
        if prime_number == number:
            return True
        else:
            False


def what_question():
    number = rnumber()
    question = f'Question: {number}'
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)