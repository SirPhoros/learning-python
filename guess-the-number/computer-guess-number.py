import random


def computer_guess(number):
    low = 1
    high = number
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        while feedback not in ("h", "l", "c"):
            feedback = input(
                f"Is {guess} too high (H), too low (L), or correct (C)? "
            ).lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        computer_guess(number)


# Call the computer_guess function to start the game
computer_guess(10)
