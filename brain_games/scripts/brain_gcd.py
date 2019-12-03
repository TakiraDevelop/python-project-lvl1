from brain_games.functions import welcome, run, question
from brain_games.cli import user_name


def main():
    welcome()
    print('Find the greatest common divisor of given numbers.')
    name = user_name()
    run(name)
    question(name, 'gcd')


if __name__ == '__main__':
    main()
