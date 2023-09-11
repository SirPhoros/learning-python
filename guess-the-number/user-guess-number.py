import random

def guess(x):
    random_number = random.randint(1, x)
    number_guessed = 0
    while number_guessed != random_number:
        number_guessed = int(input(f'Guess a number between 1 and {x}: '))
        print(number_guessed)
        if number_guessed < random_number:
            print('Sorry, guess again. Too low. Try higher!')
        elif number_guessed > random_number:
            print('Sorry, guess again. Too high. lower!')

    print(f'Congratulations! You guessed the correct number, which is {random_number}.')
