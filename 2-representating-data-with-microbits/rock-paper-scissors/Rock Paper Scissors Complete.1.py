# Imports random library
import random

# create a list of play options
# This could also be done with random numbers 0,1,2
roll_options = ["ROCK", "PAPER", "SCISSORS"]

# Initialize the global roll variables
player1_roll = 0
player2_roll = 0

# Sets up black player scores
player1_score = 0
player2_score = 0

# Game round counter
game_round = 1

# Ask for number of players
num_players = 0

# Check for if setup has been run once
has_setup = False


def Setup():
    global has_setup
    global num_players
    ask_num_players = int(input('\nHow many players are playing, 1 or 2?\n'))
    num_players = ask_num_players
    has_setup = True


def generate_rolls():
    # Because the variables were initialized globally, we need to use the global keyword
    global player1_roll
    global player2_roll
    global roll_options
    global num_players
    print('\n---ROLLS---')
    if num_players == 1:
        ask_roll_p1 = input('\nPlayer 1 --- Hit enter to roll.\n')
        if ask_roll_p1 == '':
            player1_roll = roll_options[random.randint(0, 2)]
            print('\nPlayer 1 rolled a: ', player1_roll)
            player2_roll = roll_options[random.randint(0, 2)]
            print('The computer rolled a: ', player2_roll)
    else:
        ask_roll_p1 = input('\nPlayer 1 --- Hit enter to roll.\n')
        if ask_roll_p1 == '':
            player1_roll = roll_options[random.randint(0, 2)]
            print('\nPlayer 1 rolled a: ', player1_roll)
        ask_roll_p2 = input('\nPlayer 2 --- Hit enter to roll.\n')
        if ask_roll_p2 == '':
            player2_roll = roll_options[random.randint(0, 2)]
            print('Player 2 rolled a: ', player2_roll)


def check_winner():
    #  RPS Get Final Score / End Game
    global player1_score
    global player1_score
    global num_players
    print("\n---SCORE UPDATE---")
    if num_players == 1:
        print("\nPlayer 1's score is: ", player1_score)
        print("\nThe computer's score is: ", player2_score, '\n')
    else:
        print("\nPlayer 1's score is: ", player1_score)
        print("\nPlayer 2's score is: ", player2_score, '\n')
    has_won = False
    while has_won == False:
        if player1_score == 3:
            has_won = True
            print('\nPlayer 1 has won!')
            quit()
        elif player2_score == 3:
            has_won = True
            print('\nPlayer 2/AI has won!')
            quit()
        else:
            print('\n---GET READY FOR THE NEXT ROUND---\n')
            Main()


def Main():
    global player1_roll
    global player1_score
    global player2_roll
    global player2_score
    global game_round
    global num_players
    # Runs setup once
    if has_setup == False:
        Setup()
    # Generate the rolls for this turn
    print('\n\n**************************************************\n\n')
    print('\n---ROUND ', game_round, '---\n')
    generate_rolls()
    # Main check on player turn
    if player1_roll == player2_roll:
        print("Tie!")
    elif player1_roll == "ROCK":
        if player2_roll == "PAPER":
            print(player2_roll, "covers", player1_roll)
            player2_score = player2_score + 1
        else:
            print(player1_roll, "smashes", player2_roll)
            player1_score = player1_score + 1
    elif player1_roll == "PAPER":
        if player2_roll == "SCISSORS":
            print(player2_roll, "cuts", player1_roll)
            player2_score = player2_score + 1
        else:
            print(player1_roll, "covers", player2_roll)
            player1_score = player1_score + 1
    #player1_roll == "SCISSORS"
    else:
        if player2_roll == "ROCK":
            print(player2_roll, "smashes", player1_roll)
            player2_score = player2_score + 1
        else:
            print(player1_roll, "cuts", player2_roll)
            player1_score = player1_score + 1

    game_round = game_round + 1
    check_winner()


Main()
