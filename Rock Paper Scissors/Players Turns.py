# Imports random library
import random

# create a list of play options
# This could also be done with random numbers 0,1,2
roll = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer and player
player1_roll = roll[random.randint(0, 2)]
player2_roll = roll[random.randint(0, 2)]


# Sets up black player scores
player1_score = 0
player2_score = 0

# Main check on player turn
if player1_roll == player2_roll:
    print("Tie!")
elif player1_roll == "Rock":
    if player2_roll == "Paper":
        print("You lose!", player2_roll, "covers", player1_roll)
    else:
        print("You win!", player1_roll, "smashes", player2_roll)


# TODO: Reassign rolls at the end of the turn
# TODO: Finish If Else statements to check for all possibilities
# TODO: Add in player switching, can be done on button press
