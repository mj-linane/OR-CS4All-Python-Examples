---
title: 'Sprite Overlaps and Events'
author: 'MJ Linane'
date: '10-07-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview: Sprite Overlap & Events

We use ``||sprites:kind||`` to give a label to our sprites so we can define how one ``||sprites:kind||`` of sprite will react when moving on top of another ``||sprites:kind||`` of sprite.

By making several cloud shaped sprites with the same ``||sprites:kind||`` of `Cloud`, we can write code so that all of the clouds interact with the ``Helicopter`` in the same way with an overlap event.

In Python, we would identify a `kind` with the keyword `class` followed by the name of the class object name. So it would look like: `class Student`.

In this activity, you will continue to work with:

* ``||sprites:on overlap event||`` with a ``||sprites:kind||`` applied to several identical sprites
* Overlap events

## Project #1: `SpritesKind` Overlap Event "bump" action

[Link to Video](https://aka.ms/40544a-overlap2bumpfinal)

Having sprites bump rather than pass over each other is useful game behavior for a `SpritesKind` overlap event. One way to simulate a bump is:

1. Move the sprite in the opposite direction after the overlap (we will make it bump backwards). The faster we bump, the farther we move away from the overlap object
2. Stop the sprite
    * Set `vx` and `vy` to 0
    * Change x position by `(-1) * sprite.vx`
    * Change y position by `(-1) * sprite.vy`
3. Shake the stationary object (cloud)
    * Move 1 pixel (in any direction)
    * `pause()` for a number of milliseconds
    * Move back

## 1.1 Setup Project `copter_bump1` (Bump action from overlap event)

1. Review the code below
2. Create a new project and name it `copter_bump1`
3. Create the sample code and run the code
4. Look at the overlap event - note which sprite is named `sprite` and which is named `other_sprite`, and how the code creates the bump behavior

```python
@namespace
class SpriteKind:
    Helicopter = SpriteKind.create()
    Cloud = SpriteKind.create()
    LandingPad = SpriteKind.create()
# Control the copter with the + pad

def on_right_pressed():
    copter.vx += 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    copter.vx += -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_up_pressed():
    copter.vy += -1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    copter.vy += 1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap(sprite, other_sprite):
    sprite.x += -1 * sprite.vx
    sprite.y += -1 * sprite.vy
    sprite.vx = 0
    sprite.vy = 0
    other_sprite.y += -1
    pause(100)
    other_sprite.y += 1
sprites.on_overlap(SpriteKind.Helicopter, SpriteKind.Cloud, on_on_overlap)

game.splash("Cloud Bump", "control pad flying")
scene.set_background_color(9)
copter = sprites.create(img("""
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . f f f f . . . . . .
        . . . . . f f f f . . . . . . . . . f f f f f f f . . . . . . .
        . . . . . . . f f f f f f f f f f f f f . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . e f . . e e e . . . . . . . . . . .
        . . . . f . . . . . . . . . e . . e e f f 1 1 . . . . . . . . .
        . . f f f f f f f f . . . . e e e 2 f . 1 1 1 1 . . . . . . . .
        . . . . . f . . . . . . e e e 2 2 2 f 1 1 1 1 1 . . . . . . . .
        . . . . . f . . . e e e 2 2 2 2 2 2 f 1 1 1 1 1 e . . . . . . .
        . . . . . f e e e e 2 2 2 2 2 2 2 2 f f 1 1 f 2 e . . . . . . .
        . . . . . e e 2 2 2 2 2 2 2 2 2 2 2 f f f f f 2 e . . . . . . .
        . . . . . e 2 2 2 2 2 2 2 2 2 2 2 2 f f f f f 2 e . . . . . . .
        . . . . . e e 2 2 2 2 2 2 2 2 2 2 2 f f f f f 2 e . . . . . . .
        . . . . . . e e 2 2 2 2 2 2 e 2 2 2 2 2 2 f f 2 e . . . . . . .
        . . . . . . . e e 2 2 2 2 2 e e 2 2 2 2 2 2 2 e e . . . . . . .
        . . . . . . . . e e e e 2 e e e 2 2 2 2 2 2 e e . . . . . . . .
        . . . . . . . . . . . f e . . . e e e e e e . . . . . . . . . .
        . . . . . . . . . . . f . . . . . . . . f . . . . . . . . . . .
        . . . . . . f . . . . f . . . . . . . . f . . . . . f . . . . .
        . . . . . . f f f f f f f f f f f f f f f f f f f f . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Helicopter)
copter.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
# Create and place "clouds"  Sprites
cloud1 = sprites.create(img("""
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
    """),
    SpriteKind.Cloud)
cloud1.x = 20
cloud1.y = 30
cloud2 = sprites.create(img("""
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
    """),
    SpriteKind.Cloud)
cloud2.x = 50
cloud2.y = 65
cloud3 = sprites.create(img("""
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
    """),
    SpriteKind.Cloud)
cloud3.x = 100
cloud3.y = 40
landing = sprites.create(img("""
        5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8
        5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8 5 8
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . f f . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    """),
    SpriteKind.LandingPad)
landing.y = 125
```

### 1.2: Soft Landing

There is a "T" shaped landing area at the bottom of the example. The helicopter sprite should not go through the landing pad, it should land!

1. add an `on overlaps` event for when the helicopter overlaps with the landing (note the `SpriteKind.LandingPad`)
2. The block of code in the overlap event should stop the helicopter velocity motion (setting both `vx` and `vy` to zero) and then change the helicopter position **up** 2 pixels so it isn't overlapping any more

### 1.2 Optional Challenge

 1. Add a new sprite and `SpriteKind` to the screen (for example, a mountain or a tree)
 2. set the overlap action to make the helicopter sprite have an erratic motion after an overlap. This should require 3 or more changes in position and/or velocity

#### Challenge hint

To add an additional SpriteKind, you need to add it to the `class SpriteKind` at the top of the program.

```python
class SpriteKind:
    Helicopter = SpriteKind.create()
    Cloud = SpriteKind.create()
    LandingPad = SpriteKind.create()
```

Erratic motion can be made by changing the sprite position back and forth multiple times. Try changes in velocity and/or position separated by short pauses.

### 1.3 Add a new unique sprite with `SpriteKind.Cloud`

Add a new sprite that looks nothing like a cloud (for example, a hat or a tree)

We do this by adding the code `SpriteKind.Cloud` as the last parameter in our `sprites.create()` function.

```python
something = sprites.create(img(""""""), SpriteKind.Cloud)
```

1. Position the new sprite so it is not touching any other sprite
2. add another Sprite that looks different from the previous new sprite and give it a `SpriteKind` other than `Cloud` and make sure it has a unique overlap event action (e.g. - might say something new)
3. Test the overlaps on the new sprite(s)

## Discussion

1. How can using `SpritesKind` improve code (for example, how it can make programming easier, more powerful, more efficient, ...)?
2. Why in creating a "bump" effect negative `X` and `Y` velocities are used to change the `X` and `Y` positions?
