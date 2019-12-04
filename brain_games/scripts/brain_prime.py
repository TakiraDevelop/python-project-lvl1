from brain_games.functions import welcome, run, question
from brain_games.cli import user_name


def main():
    welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = user_name()
    run(name)
    question(name, 'prime')


if __name__ == '__main__':
    main()
