from brain_games.functions import run, welcome
from brain_games.cli import user_name


def main():
    welcome()
    name = user_name()
    run(name)


if __name__ == '__main__':
    main()
