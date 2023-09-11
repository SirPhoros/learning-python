import random

def guess(x):
    random_number = random.randint(1, x)
    number_guessed = 0
    guess_count = 0

    while number_guessed != random_number:
        try:
            guess_count += 1
            number_guessed = int(input(f'Guess a number between 1 and {x}: '))

            if number_guessed < random_number:
                print('Sorry, guess again. Too low. Try higher!')
            elif number_guessed > random_number:
                print('Sorry, guess again. Too high. Try lower!')

        except ValueError:
            print('Invalid input. Please enter a valid number.')

    print(f'Congratulations! You guessed the correct number, which is {random_number}.')
    print(f'You took {guess_count} guesses.')

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        guess(x)

# Call the guess function to start the game
guess(10)
