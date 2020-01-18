import prompt


def user_name():
    name = prompt.string('May I have your name? ')
    return name


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer