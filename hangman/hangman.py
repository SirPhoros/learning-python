import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list provided
    while '-' in word or ' ' in word:
        word = random.choice(words) 

        return words.upper()
