---
title: 'While Loop MakeCode Exercises'
author: 'MJ Linane'
date: '10-27-2020'
---

## Concept: While loops

`if` and `else` conditions allows for the development games and programs that properly respond to different states and conditions - however, the condition only occurs a single time. The `while` loop allows for conditions to be checked an indefinite number of times, until the condition becomes false - effectively serving as a looping `if` statement.

In this activity, you will:

* Use `while` loops

Using `while` loops allows for actions and tasks that repeat until certain conditions are met. One example of this can be found in making a game based off of guessing a number.

### Example #1: guessing_game

1. Review the code below
2. Create the sample code and run the code
3. Identify why the code runs until the player guesses the correct answer

```python
guess = 0
value = randint(1, 5)
game.splash("I'm thinking of a number between 1 and 5")
while guess != value:
    guess = int(game.ask_for_string("What's your guess"))
game.splash("Correct!")
game.over(True)
```

This game requires the player to guess a number that the game has chosen. The game generates a random number, and then prompts the player to guess until they get it right.

Another way to think about this task is that we want the code that prompts the player to guess to keep looping **while** they are getting the answer wrong.

In English, the difference between "until" *some condition* and "while" *some condition* is simply that they are opposites.

Example: "We want to run this code until the player guesses it correctly" is the same as saying "we want to run this code while the player guesses it incorrectly".

## Project #1: checking_math

```python
guess = 0
value = randint(1, 5)
game.splash("I'm thinking of a number between 1 and 5")
while guess != value:
    guess = int(game.ask_for_string("What's your guess"))
game.splash("Correct!")
game.over(True)
```

1. Create a new project called: `while_checking_math`
2. Put in the sample code above
3. Create a new variable called `second_value` and give it a random value between 1 and 5.
4. Change the `game.splash()` screen from "I'm thinking of a number between 1 and 5" to "Answer the question!"
5. Change the while loop to check for the result of `value + second_value` instead of just `value`
6. Change the `int(game.ask_for_string()` value to instead ask for the sum of `value` and `second_value` (make sure to include what those two values are in the message)

## Project #2: fireballs

1. Create a new project called `while_fireballs`.
2. Add the following code to your project.

```python
@namespace
class SpriteKind:
    Fireball = SpriteKind.create()
    Fire = SpriteKind.create()
    FireSource = SpriteKind.create()

fire_source = None

def on_a_pressed():
    info.stop_countdown()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, other_sprite):
    info.change_life_by(5)
    other_sprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.FireSource, on_on_overlap)

def on_on_created(sprite):
    sprite.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
sprites.on_created(SpriteKind.FireSource, on_on_created)

my_sprite = sprites.create(img("""
        . . . . . . . f f f . . . . . .
        . . . . . . f 4 4 4 f . . . . .
        . . . . . f 4 4 4 4 4 f . . . .
        . . . . f 4 4 2 2 4 4 4 f . . .
        . . . . f 4 4 2 2 2 4 4 4 f . .
        . . . f 4 4 2 2 2 2 2 4 4 f . .
        . . . f 4 4 2 2 2 2 2 2 4 4 f .
        . . . f 4 4 2 2 2 5 5 2 4 4 f .
        . . f 4 4 4 2 2 2 5 5 5 4 4 4 f
        . f 4 4 4 2 2 2 5 5 5 5 4 4 4 f
        f 4 4 2 2 2 2 5 5 5 5 5 5 4 4 f
        f 4 4 2 2 2 2 5 5 5 5 5 5 4 4 f
        . f 4 4 4 2 2 5 5 5 5 5 5 4 f .
        . . f 4 4 4 4 4 4 4 4 4 4 4 f .
        . . . f 4 4 4 4 4 4 4 4 f f . .
        . . . . f f f f f f f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(my_sprite, 50, 50)
my_sprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(15)
info.start_countdown(3)

def on_update_interval():
    global fire_source
    fire_source = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . 2 2 2 2 2 2 . . 5 . . . . .
            . . 2 . . . . 2 2 5 . . . . . .
            . . 2 . . . . 2 2 2 . . . . . .
            . . 2 2 2 2 2 2 2 2 . . . . . .
            . . 2 f 2 2 2 2 f 2 . . . . . .
            . . 2 2 f 2 2 f 2 2 . . . . . .
            . . 2 2 2 f f 2 2 2 . . . . . .
            . . 2 2 2 f f 2 2 2 . . . . . .
            . . 2 2 2 f f 2 2 2 . . . . . .
            . . 2 2 2 f f 2 2 2 . . . . . .
            . . 2 2 f 2 2 f 2 2 . . . . . .
            . . 2 f 2 2 2 2 f 2 . . . . . .
            . . 2 2 2 2 2 2 2 2 . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """),
        SpriteKind.FireSource)
game.on_update_interval(500, on_update_interval)
```

This is a game in which the object is to keep throwing fireballs for as long as you can. The player's `info.score()` is how many fireballs they have launched. The problem for the player is that they have a limited number of fireballs, which are stored as `info.life()`, and need to pickup fuel in order to get more.

An important part is missing, though: the code that will fire the fireballs when the player says to start!

### Add fireballs

1. To start, add in the code to fire a single fireball from `my_sprite` in the `def on_a_pressed()` function. This should:
    * Use an `if` statement to check that the player has more than one life
    * Create a sprite of a fireball with the origin set to `my_sprite` (along with some initial velocities)
    * Decrement `info.life()` by 1
    * Increment `info.score()` by 1
2. Replace the `if` statement from part 2 with a `while` loop, so that the projectiles continue **until** the player runs out of life.

Why did we use a `while` loop instead of a ``||loops:repeat||`` loop?

The intention of the game is for the fires to keep being created until the game ends, once the player presses the A button.

A `for` loop is intended to be used to repeat something a pre-determined number of times. Using a `while` loop is very useful in this case to more accurately reflect what the developer intends.
