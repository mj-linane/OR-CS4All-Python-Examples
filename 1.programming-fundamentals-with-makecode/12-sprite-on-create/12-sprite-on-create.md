---
title: 'Sprite On Create'
author: 'MJ Linane'
date: '10-07-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview: Generate Sprites using `sprites.create()` and `sprites.on_created()`

Many games need to spawn sprites for the player to do things like collect coins or avoid oil spills. We can spawn more sprites with the built-in function `sprites.create()` and then give it actions to take the instant it is created with `sprites.on_created()`. `sprites.on_created()` is setup so that we perform those actions for *every* sprite that is created with that same type.

## Concepts

- writing functions
- calling functions
- functions with parameters
- calling functions with parameters

## Example 1: Create with on created event

[Link to Video](https://youtu.be/XR8DmTOdgNc)

### 1.1: Setup Project `spawn_cloud`

This example uses the `sprites.create` and `sprites.on_created()` functions to generate new clouds.

1. Review the code below
2. Create a new project and name it `spawn_cloud`
3. Copy and paste the sample code below and run the code

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

### How it works

We want to create clouds but don't want to set their sprite at the start. Therefore, the code starts with a variable called `cloud` but it gets an empty sprite.

```python
cloud = sprites.create(img("""
    """),
    SpriteKind.Cloud)
```

#### Creating New Sprites And Adding In `sprites.on_created()`

The `sprites.create()` function creates a cloud and we adding `SpriteKind.Cloud` to the end to give it a class of `Cloud`.

```python
cloud = sprites.create(img("""
    """),
    SpriteKind.Cloud)
```

We add to the end, a comma `,` and then we name the sprite's `SpriteKind` using dot notation.

#### Adding Sprite Actions After Creation

The code then calls a function called `def on_created()` that runs once when the cloud is created.

```python
ef on_on_created(newCloud):
    newCloud.set_image(img("""
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
    newCloud.x = randint(16, scene.screen_width() - 16)
    newCloud.y = randint(20, scene.screen_height() - 75)
sprites.on_created(SpriteKind.Cloud, on_on_created)
```

This then sets the image and a random position for newly generated sprites.

### Project 1: `spawn_clouds`

The on created event allows us to set code to run whenever a new sprite is created. This is used to create new clouds multiple times with the same code. Now we will create new clouds with by creating new variables with empty image editors.

1. Start with example code
2. Add two more set cloud to blocks for clouds
3. Add a new set `my_sprite` for a different `SpriteKind`. Write a `on_created()` function that:
   1. set an image for the sprite that is created (for example, a bird or a butterfly)
   2. set the sprite to be in a random position
4. Create at least 5 more variables that use that `SpiteKind`

Hint:
If writing a new `on_created()` function in Python, you can't have the same `on_created()` name for both because Python does not allow you to have 2 functions with the same name. We will have to give it another name. If you switch to blocks to complete this step and switch back to python, you will see that MakeCode automatically adds a number to `on_created()`. So the second on created event will be: `on_on_created2()`. I am not sure why MakeCode decided to go with this approach and unless you are comfortable, it maybe easier to simple handle `on_created()` events using the blocks.

### Project 1 Optional Challenge

1. Create an event for the `Helicopter` overlap with the new `SpriteKind`
2. Add an action that gives the new `SpriteKind` a fast velocity so that it will fly off the screen after they overlap

## Discussion

1. How is a `SpriteKind` label used in generating a sprite by creating an empty sprite variable?
2. What the `def on_on_created()` code do for you?
