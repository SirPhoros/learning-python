import random

def guess(x):
    random_number = random.randint(1, x)
    number_guessed = 0
    while number_guessed != random_number:
        number_guessed = int(input(f'Guess a number between 1 and {x}: '))
        print(number_guessed)

guess(10)    