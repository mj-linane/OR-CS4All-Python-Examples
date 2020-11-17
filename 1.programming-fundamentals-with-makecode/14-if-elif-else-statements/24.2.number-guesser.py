# Guess My Number Game

"""
PSEUDOCODE
pick a random Number 1-100
ask the player for a guess
set the number of guesses to 1
while the player guess does not equal the number
  if the player guess is greater than number, 
    tell player to guess lower
  otherwise
    tell player to guess higher
  get a new guess from the player
  increase number of guesses by 1

congratulate the player on guessing correctly
tell the player how many times it took to guess
"""

import random

print("Welcome to the random number guesser")
print("Guess the right number between 1 and 100")

# setup the variables
correct_num = random.randint(1, 100)
user_num = int(input("Make a guess: "))
attempts = 1

# Main loop
while user_num != correct_num:
    print("Correct Number: ", correct_num)
    # Give hints
    if user_num > correct_num:
        print("Guess lower")
    else:
        print("Guess higher")
    attempts += 1
    user_num = int(input("Make a guess: "))

print("Congratulations on guessing the right number!")
print("It took you " + str(attempts) + " attempts to guess correctly.")
