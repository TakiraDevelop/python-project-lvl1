from brain_games.functions import welcome, question, run
from brain_games.cli import user_name


def main():
    welcome()
    print('Answer "yes" if number even otherwise answer "no".')
    name = user_name()
    run(name)
    question(name, 'even')


if __name__ == '__main__':
    main()
