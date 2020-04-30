#  RPS Get Final Score / End Game
player1_score = 3
player2_score = 0

check_winner()


def check_winner():
    has_won = False
    while has_won == False:
        if player1_score > 2:
            has_won = True
            print('Player 1 has won!')
        if player2_score > 2:
            has_won = True
            print('Player 2 has won!')