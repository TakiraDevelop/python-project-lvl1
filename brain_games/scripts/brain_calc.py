from brain_games.functions import welcome, run, question
from brain_games.cli import user_name


def main():
    welcome()
    print('What is the result of the expression?')
    name = user_name()
    run(name)
    question(name, 'calc')


if __name__ == '__main__':
    main()
