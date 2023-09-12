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
    