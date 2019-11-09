from random import randint

from brain_games.cli import user_name, user_answer

def rnumber():
    number = randint(1,100)
    return number

def welcome():
    print('Welcome to the Brain Games!')

def run():
    name = user_name()
    print('Hello,',name + '!')

def correct_answer(number):
    if number%2 == 0:
        return 'yes'
    elif number%2 != 0:
        return 'no'
    

def question(name):
    m = 0
    while m < 3:
        number = rnumber()
        print('Question: ' + str(number))
        answer = user_answer()
        if correct_answer(number) == answer:
            print('Correct!')
            m += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer(number)}'
Let`s try again, {name}!""")
            break
    