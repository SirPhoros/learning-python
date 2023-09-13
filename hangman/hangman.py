import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list provided
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def display_word(word, used_letters):
    return " ".join([letter if letter in used_letters else "-" for letter in word])


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word

    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # keep track of what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # lives left
        print(f"You have {lives} lives left.")

        # letters used
        print("You have used these letters: ", " ".join(used_letters))

        # what current word is:
        print("Current word:", display_word(word, used_letters))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()


hangman()
