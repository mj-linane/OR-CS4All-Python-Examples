---
title: 'Sprite Motion and Events'
author: 'MJ Linane'
date: '10-06-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview

Motion is the change in position. To get sprites moving, we will change their position using a game pad event. The game pad has ``controller:controller events`` for the ``controller:up``, ``controller:down``, ``controller:left`` and ``controller:right`` buttons.

We can use those events to change sprite location, and to make the sprite move. We will also see how to give a sprite a speed of motion, or velocity. Velocity is the rate of change of our position - in real life, this is often measured as kilometers per hour or miles per hour.

When the velocities of a sprite are not zero, then the sprite will be in motion.

In these activities, the student will use:

* Controller events
* Incrementing `sprites:x` and `sprites:y` coordinates
* Setting `sprites:vx` and `sprites:vy` velocity
* Short methods and functions with motion
* `sprites:stay in screen`
* Flipping (and switching) images

## Project 1: motion_lr

### 1.1: Setup Project - motion_lr

[Link to Video](https://aka.ms/40544a-spritemoevent1)

1. Review the code below
2. Create a new project and name it `motion_lr`
3. Create the sample code and run the code

```python
def on_left_pressed():
    agent.x += -3
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    agent.x += 3
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

agent = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . 6 6 6 6 . . . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . . . 6 6 6 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
```

### 1.2: Increment position Y-axis (up and down)

1. Add additional code to control the up and down (`Y` direction) motions using the controller

### 1.3: Optional Challenges

1. Add an ``controller:A`` button event to move the sprite to the center of the game screen
2. Add a ``controller:B`` button event to make the sprite "jump" (move) `15 pixels`

## Project 2: Sprite Motion Velocity

[Link to Video](https://aka.ms/40544a-spritemoevent2velocity)

Velocity is speed in a particular direction. In our games we typically track movement in `X` and `Y` directions.

If we have a positive `X` velocity, for example, then our sprite will continue to increase in `X`, making it move to the right across the screen.

### 2.1: Setup Project - velocity_lr

1. Review the code below
2. Create a new project and name it “Velocity LR”
3. Create the sample code and run the code

```python
def on_left_pressed():
    agent.vx += -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    agent.vx += 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

agent = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . 6 6 6 6 . . . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . . . 6 6 6 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
```

### 2.2: Increment Velocity Up and Down

1. Add additional code to control the up and down (`Y` direction) velocities using the controller

### 2.3: Optional Challenges

1. Add an ``controller:A`` button event move the sprite to the center of the game screen
2. Add a ``controller:B`` button event to stop the sprite (all velocities = 0)

## Project 3: Shorter dy and dx approach

[Link to Video](https://aka.ms/40544a-spritemoevent3shortmethod)

We have created motion by capturing the key pad events and incrementing (or decrementing) a location coordinate or a velocity. Now that we have seen how this works for the four directional buttons, we can use a shorter method to handle this.

### 3.1: Setup Project - motion_short_method

1. Review the code below
2. Create a new project and name it `motion_short_method`
3. Create the sample code and run the code
4. Note the `def on_on_update():` function; this is used to assign code to run whenever the game updates. Whatever is tabbed beneath it, will run every time the game updates.
5. The following lines is `game.on_update(on_on_update)`. This simply runs our `on_on_update()` when the game starts.

```python
scene.set_background_color(1)
ball = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . 6 6 6 6 . . . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 . . . . .
            . . . . 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . 6 6 6 6 6 6 6 6 6 . . . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . . . 6 6 6 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)

def on_on_update():
    ball.x += controller.dx()
    ball.y += controller.dy()
game.on_update(on_on_update)
```

### 3.2: Create Velocity Motion

In the `on_on_update` function, add the following code:

```python
    controller.move_sprite(ball, 100, 100)
```

### 3.3: Make the sprite stay in the screen boundary

We can do this by setting `True` the setting built into MakeCode that will keep our sprite contained within the screen edges.

```python
ball.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
```

### 3.4: Optional Challenge

1. Add button events that stop the sprite's motion, and reset the sprite to the center of the screen

## Project 4: Flip Image

[Link to Video](https://aka.ms/40544a-spritemoevent4flip)

By making a mirror flip of a sprite we can simulate walking by making each leg appear differently.

### 4.1 Setup Project - flip_image

Flipping an image creates a mirror image when we create a function called `def flip_horizontal()`. This can be useful in creating a simple 2 frame walking animation.

1. Review the code below
2. Create a new project and name it `flip_image`
3. Create the sample code and run the code

```python
scene.set_background_color(6)
my_sprite = sprites.create(img("""
        ................................
            ..............2.................
            ............22222...............
            ...........2222222..............
            ..........222222222.............
            ..........227222722.............
            .........22222822222............
            ..........222288222.............
            ..........222222222.............
            ...........2299222..............
            .......444442222244444..........
            .......444444424444444..........
            .......444444444444444..........
            .......444444444444444..........
            .......444.4444444.444..........
            .......444.4444444.444..........
            .......444.4444444.444..........
            .......444.4444444.444..........
            .......444.4444444.aaa..........
            .......444.4444444.a.a..........
            .......aaa.4444444.aaa..........
            .......a.a.4444444..............
            .......aaa.77....77.............
            ...........77....77.............
            ...........77....77.............
            ...........77....77.............
            ...........77....77.............
            ...........77....77.............
            ...........77....77.............
            ..........ddd....77.............
            .................77.............
            ................ddd.............
    """),
    SpriteKind.player)
```

### 4.2: Image Flip with motion

1. Make your own image move using the ``controller:up``, ``controller:down``, ``controller:left``, `controller:right` buttons on the controller
2. Use `controller:A` button to run the code `flip_horizontal` to flip the image left and right.

```python
def on_a_pressed():
    flip_horizontal()

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
```

### 4.3: Optional Challenge

Add code and use `controller:B` button to flip the image upside down.

## Discussion Questions

1. How events can be used to run code using an example.
2. What is the difference between changing position and changing velocity.
3. When using `flip_horizontal()` in project #4, the variable `my_sprite` is not what is flipped. What is actually flipped? (Hint: Look at the sprite image code in python. It doesn't change)
