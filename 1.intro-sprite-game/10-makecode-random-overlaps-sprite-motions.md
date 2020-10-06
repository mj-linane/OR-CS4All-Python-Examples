---
title: 'Random Overlaps and Sprite Motions'
author: 'MJ Linane'
date: '10-06-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Project 1: Random Overlaps

### Setup Project - sprite_overlap

[Link to Video](https://aka.ms/40544a-randompositionoverlap)

1. Create a new project called `sprite_overlap_random`
2. Enter in the sample code below

```python
@namespace
class SpriteKind:
    Hat = SpriteKind.create()

def on_a_pressed():
    my_sprite.set_position(randint(15, 145), randint(15, 105))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, other_sprite):
    sprite.say("Excuse Me!", 500)
    # Add some code that makes the sprite or other_sprite do something with random
    # Add some code that makes sprite or other_sprite say something

sprites.on_overlap(SpriteKind.player, SpriteKind.Hat, on_on_overlap)

hat = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            .......4444444444...............
            .......4777777774...............
            .......4777777774...............
            .......4777777774...............
            .......4777777774...............
            .......4777777774...............
            .......4777777774...............
            .......444444444444444444.......
            .......666666666................
            .......666666666................
            .......646666666................
            .....66666666666................
            .....66666666666................
            .....66666666666................
            ......6666666666................
            ......6666666666................
            .......666666666................
            ......6666666666................
            ......6666666666................
            ......666666666.................
            ......666666666.................
            ................................
            ................................
            ................................
            ................................
    """),
    SpriteKind.Hat)

my_sprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . 5 . . 5 . . 5 . . . . . .
            . . . . 5 . 5 . 5 . . . . . . .
            . . . . . 5 7 5 . . . . . . . .
            . . . . 5 7 2 7 5 . . . . . . .
            . . . . . 5 7 5 . . . . . . . .
            . . . . . . 5 . . . . . . . . .
            . . . . . . 1 . . . . . . . . .
            . . 2 1 1 1 1 1 1 1 2 . . . . .
            . . . . . . 1 . . . . . . . . .
            . . . . . . 1 . . . . . . . . .
            . . . . . . 1 . . . . . . . . .
            . . . . . 1 . 1 . . . . . . . .
            . . . . 7 . . . 7 . . . . . . .
            . . . 7 . . . . . 7 . . . . . .
            . . 2 2 . . . . . 2 2 . . . . .
    """),
    SpriteKind.player)

my_sprite.set_position(randint(15, 145), randint(15, 105))
hat.set_position(35, 60)
```

### 1.2: Check for random overlap with many sprites

Starting with the example, where the game randomly moves 2 sprites with button pushes

### 1.3: Add sprites

Add at least 2 more sprites with random or fixed position

### 1.4: Add overlap code

Add the following code:

```python
def on_on_overlap(sprite, other_sprite):
    # Add some code that makes the sprite or other_sprite do something with random
    # Add some code that makes sprite or other_sprite say something

sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)
```

Add code to the overlap code that will:

1. results in a new behavior that uses `randint()`. For example, set velocity, set location, change location by, and so on.
2. causes the sprite or other_sprite to say something

### 1.5: Test

Test to see if sprites overlap works with different sprites of the same kind.

### 1.6: Optional Challenge

1. Make multiple sprites randomly change position with the `a` button
2. Give two of the sprites a random velocity. Set the `randint` range across negative and positive for `vx` and `vy`. For instance: `my_sprite.set_velocity(randint(-50, 50), randint(-50, 50))`
