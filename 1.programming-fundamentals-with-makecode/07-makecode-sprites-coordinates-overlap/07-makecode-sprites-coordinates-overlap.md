---
title: 'Control Sprites'
author: 'MJ Linane'
date: '09-30-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Topic #1: Coordinates & Walker

### Project #1: Identify the X, Y coordinates of the Game Screen

In this activity, you will investigate the game screen.

Move a walker sprite around the game screen, and use it to identify `X` and `Y` coordinates.

In order to create games, we need to be able to place `sprites` and other objects at various locations on the game screen. In this set of activities, we will relate the screen (`x`, `y`) coordinates to the 4 corners and middle of the game screen.

### Step #1: Coordinate Walker

Use the coordinate walker example to move around the screen and track `X` and `Y` coordinates.

Use this code in the simulator to complete the tasks.

```python
def on_a_pressed():
    game.splash("X=" + str(player1.x) + " Y=" + str(player1.y))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

player1: Sprite = None
game.splash("Sprite Walker", "\"A\" for coordinates")
player1 = sprites.create(img("""
        1 1 1
            1 2 1
            1 1 1
    """),
    SpriteKind.player)
scene.set_background_color(12)

def on_on_update():
    player1.x += controller.dx()
    player1.y += controller.dy()
    if player1.x < -10:
        player1.x = -10
    if player1.x > 170:
        player1.x = 170
    if player1.y < -10:
        player1.y = -10
    if player1.y > 130:
        player1.y = 130
game.on_update(on_on_update)
```

1. To check the location: run the program, and then press the `controller A` button on the game pad (or space bar key on keyboard). This will display the starting location's `X` and `Y` coordinates.
    * Note the two coordinate values for `(X, Y)`
2. Move the sprite: click on the game pad (or use keyboard `WASD` keys) to move the sprite. Check the coordinates after moving.

### What we learned

Use `X` and/or `Y` in your answers

1. Describe how coordinates change when moving up and down. Which direction caused the coordinates to increase?
2. Describe how coordinates change when moving right and left. Which direction caused the coordinates to increase?

### Student Task #2: Map Game Screen

Use the Jamboard class activity

## Topic 2: Sprites Overlap

### Project #2: Eat Fruit

### Step 1: Add actions to overlap events
### Step 2: Ghost Off and On
### Step 3: Multiple Kinds

### Topic #3: Random

Random numbers provide an element of chance to our games that make them look and feel more natural. They can also provide surprises and introduce elements of “good” or “bad” luck.

### Project 3: Random Location
## Step 1: Random Sprite Location
## Step 2: Set random position using a button event
## Check for random overlap with many sprites