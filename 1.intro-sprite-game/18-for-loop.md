---
title: 'For Loop'
author: 'MJ Linane'
date: '10-21-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Activity: For Loops

Games often need to keep multiple variables to keep track of how well a player is doing. When programming in Python, there are many ways game code needs to increase (or decrease) a count.

We refer to increasing a count as incrementing it, and decreasing count as decrementing it.

A `for` loop is one of the most common loop structures. It allows for a consistent way to iterate a (generally) predetermined number of times.

With the for loop we can execute a set of statements, once for each item in a list.

In python, this structure is represented in two different ways: the `for index` loop, as well as the `repeat` loop. The main difference between the two was largely based on whether or not the user needed to use the index in their loop.

In Python, the structure of these loops is more complex than in python. However, this complexity allows for the structure to be suitable for a wider range of tasks.

### `for in` loop syntax

We can simply loop though something using `for in`. This type of loop *does something* to each item that it iterates through.

In the example below, we are using `letter` as a variable but you could name this any legal variable. Sometimes you will see other variables as placeholders as, `n`, `i`, `k`, `j`.

The program will go through each letter and then perform an action. Here it is simply printing out the letter.

```python
password = "password1234"

for letter in password:
  print(letter)
```

### `for in range()` loop syntax

To loop through a set of code a specified number of times, we can use the `range()` function. The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```python
for number in range(6):
  print(x)
```

In the code example above, the program will count all the numbers between 0 and the max number - 1. So `range(6)` is not the values of 0 to 6, but the values 0 to 5.

To start counting a number other than 0, we can pass in two parameters into `range()`. The first being the beginning number and the second being the end.

```python
for x in range(2,6):
  print(x)
```

The `range()` function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: `range(2, 6)`, which means values from 2 to 6 (but not including 6):

## Concept: Increase By (increment)

### Example #1: Increment with `game.on_update_interval()`

Games on MakeCode arcade run on a loop. This is called the "main game loop". We can add code that will run every time the game updates. The timing here isn't exact because it will depend on the computer hardware and its ability to refresh the screen. Slow computer = slow updates.

In the example below, we will increase score on every update. `game.on_update_interval()` takes in 2 parameters:

* the delay after the code runs
* the function to run after that amount of time has passed.

```python
count = 0

def on_update_interval():
    global count
    count += 1
    info.set_score(count)
game.on_update_interval(500, on_update_interval)

```

### Example #2: Increment to make a spiral using a `for loop`

A spiral increases the length of each side. In the example below the sides are 5, 6, 7 and 8 pixels long. To continue the spiral we will need to continue to make each side longer than the last. Notice that some of the lengths are negative values (these are in order to move up or move left).

```python
my_sprite = sprites.create(img("""
        . . . . . . . . 8 . . . . . . .
        . . . . . 8 8 8 8 8 8 8 . . . .
        . . . . 8 8 8 8 8 8 8 9 8 . . .
        . . . 8 8 8 8 8 8 8 9 9 9 8 . .
        . . 8 8 8 8 8 8 8 8 8 9 8 8 8 .
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 .
        . . . 8 8 8 8 8 8 8 8 8 8 8 . .
        . . . . 8 8 8 8 8 8 8 8 8 . . .
        . . . . . 8 8 8 8 8 8 8 . . . .
    """),
    SpriteKind.player)
for i in range(10):
    pause(200)
    my_sprite.x += 5
    pause(200)
    my_sprite.y += 6
    pause(200)
    my_sprite.x += -7
    pause(200)
    my_sprite.y += -8
```

### Example #3: Move in a spiral

We want to move a sprite in a spiral - starting small in a square like pattern, and moving further and further away as the iteration process continues. Currently, the sprite drifts up and to the left. We need to increase the distance that the sprite travels on a side for each iteration so that it moves further for each side.

1. Start with the code from example 2, add in a new variable: `increase`
2. Add math expressions like `+` and `-` to use the variable `increase` to increase the `x` distance the sprite moves on each step: `my_sprite.x += 5`
3. Increment `increase` by 5 at the end of `for in range()` loop: `increase += 5`

Part 3 might look like the code below:

```python
increase = 0
my_sprite.x += 7 + increase
increase += 5
```

The code above will cause the `x` position for `my_sprite` to move farther by 5 on each loop as `increase` becomes 5 larger each time in the loop.

So we can see the following for how one of the spiral sides moves farther each loop

>* Loop 1: my_sprite X coordinate change = **7**
>* Loop 2: my_sprite X coordinate change = 7 + 5 = **12**
>* Loop 3: my_sprite X coordinate change = 7 + 10 - **17**

## Project #1: asteroid_blast

1. Create a new project called `asteroid_blast`
2. We need to add a few extra Asteroids to make it seem like the player ran into an asteroid belt. At the end of the code, add a `for in range()` loop that starts at 0 and ends at 9.
3. Inside of the loop, add `create(sprites.space.space_asteroid0, SpriteKind.Asteroid)`. This will create 10 Asteroids. Add a `pause()` for 250 ms into the loop as well, so that the extra sprites get created over the course of 2.5 seconds.

```python
@namespace
class SpriteKind:
    Asteroid = SpriteKind.create()

def on_on_created(sprite):
    sprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
    setPosition(sprite, 10)
    setMotion(sprite)

sprites.on_created(SpriteKind.Asteroid, on_on_created)

def on_update_interval():
    sprites.create(sprites.space.space_asteroid0, SpriteKind.Asteroid)
game.on_update_interval(1500, on_update_interval)

def setMotion(asteroid: Sprite):
    asteroid.vx = randint(-8, 8)
    asteroid.vy = randint(35, 20)
def setPosition(sprite: Sprite, edge: number):
    sprite.x = randint(edge, screen.width - edge)
    sprite.y = 0


name = "Captain "
player_name = game.ask_for_string("What is your name?")
if player_name == "myName!":
    player_name += " 2"
name += player_name
intro = "Hello, "
intro += name
intro += "! This is my Space Game!"
game.splash(intro)
x = screen.width / 2
y = screen.height - 20
```
