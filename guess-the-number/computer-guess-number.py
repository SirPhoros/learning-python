import random


def computer_guess(number):
    low = 1
    high = number
    feedback = ""

    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} too high (H), too Low (L), or correct (C)? "
        ).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')  


computer_guess(10)