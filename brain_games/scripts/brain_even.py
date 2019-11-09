from brain_games.functions import run, welcome,question
from brain_games.cli import user_name
from random import randint

def main():
    welcome()
    print('Answer "yes" if number even otherwise answer "no".')
    name = user_name()
    print('Hello,',name + '!')
    question(name)

if __name__ == '__main__':
    main()
    
