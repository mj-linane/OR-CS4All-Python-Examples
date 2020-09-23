player_ties = 0
player_b_wins = 0
player_a_wins = 0

def on_up_pressed():
    global player_ties
    player_ties = player_ties + 1
    game.splash("Players Tied!")
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global player_b_wins
    player_b_wins = player_b_wins + 1
    game.splash("Player B Scored!")
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global player_a_wins
    player_a_wins = player_a_wins + 1
    game.splash("Player A Scored!")
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# game.splash("Rounds played: " + str((player_a_wins + player_2_wins + player_ties)))

def on_down_pressed():
    game.show_long_text("Rounds played: " + (str((player_a_wins + player_b_wins + player_ties)) + "\n Player A Score: " + str(player_a_wins) + "\n Player B Score: " + str(player_b_wins)),
        DialogLayout.BOTTOM)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)
