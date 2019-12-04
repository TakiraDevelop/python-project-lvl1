from brain_games.functions import welcome, run, question
from brain_games.cli import user_name


def main():
    welcome()
    print('What number is missing in the progression?')
    name = user_name()
    run(name)
    question(name, 'progression')


if __name__ == '__main__':
    main()
