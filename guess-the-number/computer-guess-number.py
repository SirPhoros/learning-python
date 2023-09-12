import random


def computer_guess():
    # Get the range of numbers from the user
    while True:
        try:
            low = int(input("Enter the lower bound of the range: "))
            high = int(input("Enter the upper bound of the range: "))
            if low >= high:
                raise ValueError("Upper bound must be greater than the lower bound")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}")

    print(f"\nGreat! The computer will now guess a number between {low} and {high}.")

    # Initialize variables
    feedback = ""
    attempts = 0

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
        computer_guess()


# Call the computer_guess function to start the game
computer_guess()
