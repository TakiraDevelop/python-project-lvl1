from random import randint, choice

from brain_games.cli import user_name, user_answer


def rnumber():
    number = randint(1, 100)
    return number


def expression():
    expression = ['+', '-', '*']
    return choice(expression)


def welcome():
    print('Welcome to the Brain Games!')


def run(name):
    print('Hello,', name + '!')


def correct_answer(question, game):
    if game == 'even':
        if question % 2 == 0:
            return 'yes'
        elif question % 2 != 0:
            return 'no'
    if game == 'calc':
        exp = question[1]
        if exp == '+':
            return question[0] + question[2]
        if exp == '-':
            return question[0] - question[2]
        if exp == '*':
            return question[0] * question[2]
    if game == 'gcd':
        a = question[0]
        b = question[1]
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a


def question(name,game):
    m = 0
    while m < 3:
        if game == 'even':
            question = rnumber()
        elif game == 'calc':
            question = calc()
        elif game == 'gcd':
            question = gcd()
        print('Question: ' + str(question))
        answer = user_answer()
        if int(correct_answer(question, game)) == int(answer):
            print('Correct!')
            m += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer(question, game)}' 
Let`s try again, {name}!""")
            break


def calc():
    first_number = rnumber()
    second_number = rnumber()
    exp = expression()
    return first_number,exp,second_number

def gcd():
    first_number = rnumber()
    second_number = rnumber()
    return first_number,second_number
    
