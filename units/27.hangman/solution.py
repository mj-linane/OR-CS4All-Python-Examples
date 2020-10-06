# Hangman Game
# The computer picks a word and the player guesses
# it one line at a time. If wrong, the little person
# will be hanged.

# imports
import random

# Constants
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']  # noqa: W605

MAX_WRONG = len(HANGMAN) - 1
WORDS = ["BEAR", "PIZZA", "SNAKE", "WASHINGTON", "MOON"]

# Initialize variables

# Pick a word
word = random.choice(WORDS)

# One dash for each lettter in a word to be guessed
current_guess = "-" * len(word)

# Tracks wrong guesses
wrong_guesses = 0

# Contains all used letters
used_letters = []

# Main loop
print("Welcome to Hangman")
print("Try to Guess The Word")

while wrong_guesses < (MAX_WRONG) and current_guess != word:
    print(HANGMAN[wrong_guesses])
    print("You have used the following letters: ", used_letters)
    print("So far, the word is: ", current_guess)

    guess = input("Enter your letter guess:")
    guess = guess.upper()

    while guess in used_letters:
        print("You have already guessed that letter", guess)
        guess = input("Enter your letter guess:")
        guess = guess.upper()

    used_letters.append(guess)

    # Check guess
    if guess in word:
        print("You guessed correctly")

        # create a new current_guess to include guess
        new_current_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]
        current_guess = new_current_guess
    else:
        print("Sorry, that is not in the word")
        # If wrong, increase wrong number by 1
        wrong_guesses += 1

# Ending the game
if wrong_guesses == MAX_WRONG:
    print(HANGMAN[wrong_guesses])
    print("You have been hanged!")
    print("The word was:", word)

else:
    print("You Won!!")
