import random


def computer_guess(number):
    low = 1
    high = number
    feedback = ""

    while feedback != "c":
        guess = random.randint(low, high)
        while feedback not in ("h", "l", "c"):
            feedback = input(
                f"Is {guess} too high (H), too low (L), or correct (C)? "
            ).lower()

        attempts += 1

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("Please enter 'H' for too high, 'L' for too low, or 'C' for correct.")

    print(
        f"\nYay! The computer guessed your number, {guess}, correctly in {attempts} attempts!"
    )

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        computer_guess(number)


# Call the computer_guess function to start the game
computer_guess(10)
