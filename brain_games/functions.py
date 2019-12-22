from random import randint, choice

from brain_games.cli import user_answer


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
        even_answer(question)
    elif game == 'calc':
        calc_answer(question)
    elif game == 'gcd':
        gcd_answer(question)
    elif game == 'progression':
        progression_answer(question)
    elif game == 'prime':
        prime_answer(question) 

def prime_answer(question):
    prime_number = 2
    while question[0] % prime_number != 0:
        prime_number += 1
        if prime_number == question[0]:
            return 'yes'
        else:
            return 'no'


def gcd_answer(question):
    a = question[0]
    b = question[1]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        return a


def calc_answer(question):
    exp = question[1]
    if exp == '+':
        return int(question[0] + question[2])
    if exp == '-':
        return int(question[0] - question[2])
    if exp == '*':
        return int(question[0] * question[2])


def progression_answer(question):
    findex = question.index('..')
    if findex >= 2:
        fnumber = question[findex - 1] - question[findex - 2]
        fnumber = fnumber + question[findex - 1]
    else:
        fnumber = question[findex + 2] - question[findex + 1]
        fnumber = question[findex + 1] - fnumber
    return fnumber


def even_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question(name, game):
    m = 0
    while m < 3:
        question = what_question(game)
        print('Question: ' + ' '.join([str(i) for i in question]))
        answer = user_answer()
        if game == 'even' or game == 'prime':
            if correct_answer(question, game) == answer:
                print('Correct!')
                m += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was""" + f"""'{correct_answer(question, game)}'
Let`s try again, {name}!""")
            break
        else:
            if int(correct_answer(question, game)) == int(answer):
                print('Correct!')
                m += 1
            else:
                print(f"""'{answer}' is wrong answer ;(. Correct answer was""" + f"""'{correct_answer(question, game)}'
Let`s try again, {name}!""")
                break


def what_question(game):
    if game == 'even':
        question = rnumber()
    elif game == 'calc':
        question = calc()
    elif game == 'gcd':
        question = gcd()
    elif game == 'progression':
        question = progression()
    elif game == 'prime':
        question = prime()
    return question


def calc():
    first_number = rnumber()
    second_number = rnumber()
    exp = expression()
    list_calc = [first_number, exp, second_number]
    return list_calc


def prime():
    number = [rnumber()]
    return number


def gcd():
    first_number = rnumber()
    second_number = rnumber()
    return first_number, second_number


def progression():
    rstep = randint(1, 10)
    progression = list(range(0, 100, rstep))
    progression = progression[0:10]
    progression[randint(0, 9)] = '..'
    return progression
