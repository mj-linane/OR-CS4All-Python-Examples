---
title: 'Sprite On Create'
author: 'MJ Linane'
date: '10-07-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview: Generate Sprites using ``||sprites:create||`` and `def on_on_created()`

Many games need to spawn sprites for the player to do things like collect coins or avoid oil spills.

We will set a new variable and then create an empty sprite with nothing in it.

```python
var = sprites.create(img("""
    """),
    SpriteKind.Cloud)
```

` block from the Sprites menu to spawn a new empty sprite, with nothing in it yet. Then we can use an `def on_on_created()` event to set the image and a random position for newly generated sprites.

The `def on_on_created()` block uses the sprite's `SpriteKind` so we can give our new sprites the exact attributes we want, like an image, velocity, or position.

## Project 1: Create with on created event

[Link to Video](https://youtu.be/XR8DmTOdgNc)

### 1.1: Setup Project `spawn cloud`

This example uses the `def on_on_created()` event function to set the sprite image and location after a sprite of a particular `SpriteKind` is spawned.

1. Review the code below
2. Create a new project and name it `spawn_cloud`
3. Create the sample code and run the code
4. Carefully examine the `SpriteKind.Cloud` code and the `def on_on_created()` event

```python
@namespace
class SpriteKind:
    Helicopter = SpriteKind.create()
    Cloud = SpriteKind.create()

def on_up_pressed():
    agent.vy += -1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_created(new_cloud):
    new_cloud.set_image(img("""
        . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . 1 1 1 1 1 8 . . . . . .
                . . . 1 1 8 8 8 1 1 1 1 1 1 . .
                . 8 1 1 8 8 8 8 8 8 8 8 8 1 1 .
                . 1 8 8 8 1 8 8 8 1 1 8 8 8 1 .
                1 1 8 8 1 1 1 1 1 8 8 8 1 1 1 .
                1 1 8 8 8 8 8 1 1 8 1 8 1 1 . .
                . 1 1 1 1 8 8 8 8 8 8 8 1 8 . .
                . . . . 1 1 8 8 1 1 8 8 1 . . .
                . . . . . . 8 8 8 1 1 1 1 . . .
                . . . . . . 1 1 1 1 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
    """))
    new_cloud.x = randint(16, scene.screen_width() - 16)
    new_cloud.y = randint(20, scene.screen_height() - 75)
sprites.on_created(SpriteKind.Cloud, on_on_created)

def on_left_pressed():
    agent.vx += -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite, other_sprite):
    sprite.x += -1 * sprite.vx
    sprite.y += -1 * sprite.vy
    sprite.vx = 0
    sprite.vy = 0
    other_sprite.y += -1
    pause(100)
    other_sprite.y += 1
sprites.on_overlap(SpriteKind.Helicopter, SpriteKind.Cloud, on_on_overlap)

def on_right_pressed():
    agent.vx += 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    agent.vy += 1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

game.splash("Generated Clouds", "on Sprite created")
scene.set_background_color(9)
agent = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ......................ffff......
            .....ffff.........fffffff.......
            .......fffffffffffff............
            ...............f................
            ...............f................
            ..............ef..eee...........
            ....f.........e..eeff11.........
            ..ffffffff....eee2f.1111........
            .....f......eee222f11111........
            .....f...eee222222f11111e.......
            .....feeee22222222ff11f2e.......
            .....ee22222222222fffff2e.......
            .....e222222222222fffff2e.......
            .....ee22222222222fffff2e.......
            ......ee222222e222222ff2e.......
            .......ee22222ee2222222ee.......
            ........eeee2eee222222ee........
            ...........fe...eeeeee..........
            ...........f........f...........
            ......f....f........f.....f.....
            ......ffffffffffffffffffff......
            ................................
            ................................
            ................................
            ................................
            ................................
    """),
    SpriteKind.Helicopter)
cloud1 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Cloud)
cloud2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Cloud)
```

### 1.2: Add More Random Clouds

The `def on_on_created(obj)` function allows us to set code to run whenever a new sprite is created. This is used to create new clouds multiple times with the same code. Now we will create new clouds with the `cloud` variable and empty sprite images.

1. Add two more `cloud` variables by adding a number to the end; `cloud2`, `cloud3`, etc
2. Add a new sprite and set it to a different `SpriteKind`. Use the `def on_on_created()` function event to
   1. set an image for the sprite that is created (for example, a bird or a butterfly)
   2. set the sprite to be in a random position
   3. Create 5 sprites using 5 different variable names but all of the same `SpriteKind`.

### Optional Challenge

1. Create an event for the `Helicopter` overlap with the new `SpriteKind`
2. Add an action that gives the new `SpriteKind` a fast velocity so that it will fly off the screen after they overlap

## Discussion

1. How is a `SpriteKind` label used in generating a sprite by creating an empty sprite variable?
2. What the `def on_on_created()` code do for you?
