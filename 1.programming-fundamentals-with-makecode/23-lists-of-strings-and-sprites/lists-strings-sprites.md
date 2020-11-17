---
title: 'Working With Lists: Tilemaps, Sprites, and Strings'
author: 'MJ Linane'
date: '11-10-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.programming-fundamentals-with-makecode\27.lists-string-sprite-tilemap'
lesson number: ''
---


In the previous lesson, we learned that lists can be used to keep track of an indefinite number of values, as well as some of the basic ways in which developers can interact with the lists.

In this lesson, we are going to practice some more with lists of specific data types.

## Lists of Strings

In this activity, we will identify some ways in which we can use lists of strings, and explore other ways in which we can use lists.

### Practice #1: princess-dialogue

1. Create a new project called `lists-princess-dialogue`
2. Copy/paste the sample code below

```python
text_list = ["Hello", "I am", "the", "Princess"]
my_sprite = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . .
        . . . . . f 5 5 5 f f . . . . .
        . . . . f 1 5 2 5 1 6 f . . . .
        . . . f 1 6 6 6 6 6 1 6 f . . .
        . . . f 6 6 f f f f 6 1 f . . .
        . . . f 6 f f d d f f 6 f . . .
        . . f 6 f d f d d f d f 6 f . .
        . . f 6 f d 3 d d 3 d f 6 f . .
        . . f 6 6 f d d d d f 6 6 f . .
        . f 6 6 f 3 f f f f 3 f 6 6 f .
        . . f f d 3 5 3 3 5 3 d f f . .
        . . f d d f 3 5 5 3 f d d f . .
        . . . f f 3 3 3 3 3 3 f f . . .
        . . . f 3 3 5 3 3 5 3 3 f . . .
        . . . f f f f f f f f f f . . .
        . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
my_sprite.say(text_list[0], 300)
pause(400)
my_sprite.say(text_list[1], 300)
pause(400)
my_sprite.say(text_list[2], 300)
pause(400)
my_sprite.say(text_list[3], 300)
pause(400)
```

In the example above, we have the sprite say something every, pause, and the say another thing off the list
 `text_list`. This is redundant. We don't want to repeat ourselves. Therefore, lets shorten it by making a `for` loop for the `text_list` sayings.

```python
for text in text_list:
  my_sprite.say(text, 300)
  pause(400)
```

1. Use a `for` loop to reduce the redundancy found in the example, without changing the behavior of the code:
2. Add (at least) three more strings to the `text_list` list, describing what she had for lunch.
3. Challenge: after the princess has given her speech, make her say it again backwards. You may find `list.reverse()` a useful Python method for completing this task

The changes in this task make the code a lot easier to read, and demonstrate a very common usage of lists - iterating over their contents.

### Practice #2: random-reactions

Another way in which you can use string lists in your games is to create reactions to different events - for example, the player running into another character, or losing a life. This can be used both to personalize your game, and to make the game feel more alive, as the characters respond ‘randomly’ to the player’s actions.

1. Create a new project called `lists-random-reactions`
2. Use the same code as `practice #1`

```python
my_sprite.say(text_list[randint(0, len(text_list) - 1)], 250)
```

Notice: we are able to get a random item off the `text_list` by accessing a random index position and getting the string in that position:  `my_sprite.say(text_list[randint(0, len(text_list) - 1)], 250)`

Also, notice that when we access the items in the list by their index position, we are using `randint(0` to start looking, but then we end looking at `len(text_list)-1)`. Why do we do that? We want to possibly get all index positions in the list. The list has 4 items in the list. But...we started to count at position `0`. So we will only have items with index positions up to `3`. If we try to look for a string in the 4th position, Python will complain because we have gone beyond the limits of the list.

1. Create another text list, stored in a different variable called `enemy_script`. Fill it with the following strings:
   1. “go away”
   2. “why are you running into me”
   3. “leave”
2. Add at least three other sprites of `SpriteKind.enemy`. Give them random x,y locations around the map when the game starts.
3. Set the player’s life to 5
4. Create an on overlap event between `SpriteKind.player` and `SpriteKind.enemy` which:
   1. causes life to `change by -1`
   2. the enemy to say a random word from `enemy_script`
   3. set the enemy to be a ghost, pause for a second and then make it so the sprite isn’t a ghost: `enemy_sprite_name.set_flag(SpriteFlag.GHOST, True)`
5. Challenge: add an on A button pressed event. When the A button is pressed, use ask for string with text and list add value to end to add a word the player chooses into text list.

## Lists of Sprites

So far we have used lists of numbers and strings. We will see that lists can be used with any variable type, including sprites.

In this activity, we will use lists of sprites to create unique behaviors for the characters in our games, as well as introduce the basics of artificial intelligence for our enemy characters.

Creating lists of sprites follow a similar process as creating lists of numbers or strings. Start with a new list (e.g.- of numbers), and then replace all of the numbers within the list with sprites.

### Practice #1: Moving all Asteroids

1. Review the code below
2. Create a new project and call it `list-sprite-lists`
3. Run the code

```python
@namespace
class SpriteKind:
    Asteroid = SpriteKind.create()

def on_a_pressed():
    for value in my_sprite_list:
        value.set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

my_sprite_list = [sprites.create(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        SpriteKind.Asteroid),
    sprites.create(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        SpriteKind.Asteroid),
    sprites.create(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        SpriteKind.Asteroid)]
```

1. Instead of moving every asteroid, select a random asteroid from my `sprite_list` and move only that asteroid when the`A button is pressed`
2. Choose another random asteroid, and have it say `"woosh"` for `300 ms`.

### Practice #2: Creating lists of sprites with `sprites.all_of_kind()`

1. Create a new project called `lists-sprites-of-kind`
2. Review and run the code below

```python
@namespace
class SpriteKind:
    Asteroid = SpriteKind.create()

def on_a_pressed():
    for value in sprites.all_of_kind(SpriteKind.Asteroid):
        value.set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

for i in range(10):
    my_sprite = sprites.create(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        SpriteKind.Asteroid)
```

Notice how we can create sprites of a certain kind using `sprites.all_of_kind(SpriteKind.Asteroid)`

We can then run a `for` loop on every sprite of that kind. We can then set its position to be a random value.

Notice, we also use the `scene.screen_width()` and `scene.screen_height` to automatically place those sprites inside of the screen boundaries.

```python
for value in sprites.all_of_kind(SpriteKind.Asteroid):
    value.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
```

### Practice #3: fireworks

1. Create a new project called `lists-fireworks`
2. Review and run the code below

```python
@namespace
class SpriteKind:
    Firework = SpriteKind.create()

def on_a_pressed():
    for i in range(30):
        projectile = sprites.create_projectile(img("""
                1
            """),
            randint(-100, 100),
            randint(-100, 100),
            SpriteKind.player,
            firework)
        firework.set_flag(SpriteFlag.GHOST, True)
        projectile.image.fill(randint(1, 14)) # Fill here is used to randomize the color of the projectiles
        firework.destroy()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

firework = sprites.create(img("""
        1 1 1
        1 2 1
        1 1 1
    """),
    SpriteKind.Firework)
firework.set_position(randint(0, scene.screen_width()), randint(0, scene.screen_height()))
firework.set_flag(SpriteFlag.GHOST, True)
```

The example above creates a firework at a random position on the screen, and then on any button press sets the firework off. The fill image with block is used to randomize the color of the projectiles, so that each firework is more magnificent. It has a few problems as written, though:

* The firework can be set off again, creating an explosion from nothing
* You can only really make one firework

Using list of sprites of kind, we can easily address both of these issues

#### Bigger and Better Fireworks

1. Add a repeat loop in the on start that will create `100` fireworks at the bottom of the script. It would look like the code below.

```python
sprite_list = []
for i in range(100):
    firework = sprites.create(img("""
            1 1 1
            1 2 1
            1 1 1
        """),
        SpriteKind.Firework)
    firework.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    firework.set_flag(SpriteFlag.GHOST, True)
```

2. Use `sprites.all_of_kind()` to get an list of all the fireworks in the `on a button pressed event`, and store it in the variable `sprite_list`
3. Add an `if` condition around the rest of the `on a button pressed`, so that the rest of the event only occurs *if the length of list `sprite_list` is greater than 0*.

```python
def on_a_pressed():
    global projectile
    global sprite_list
    sprite_list = sprites.all_of_kind(SpriteKind.Firework)
    if len(sprite_list) > 0:
```

4. Select a firework from `sprite_list` at random, and store that in the variable `origin`. Replace all references to firework in the event to refer to this new variable

```python
origin = sprite_list[randint(0, len(sprite_list) - 1)]
        for index in range(30):
            projectile = sprites.create_projectile(img("""
                    1
                """),
                randint(-100, 100),
                randint(-100, 100),
                SpriteKind.player,
                origin)
            origin.set_flag(SpriteFlag.GHOST, True)
            projectile.image.fill(randint(1, 14))
        origin.destroy()
```

5. Challenge: change the on any button pressed event to only trigger when the A button is pressed, and make a on B button pressed event that will create a new firework. Make sure to use either a function or an on created sprite of kind event to reduce the redundancy between the new event and the code in the main program.

##### Completed code without challenge

```python
@namespace
class SpriteKind:
    Firework = SpriteKind.create()

def on_a_pressed():
    global projectile
    global sprite_list
    sprite_list = sprites.all_of_kind(SpriteKind.Firework)
    if len(sprite_list) > 0:
        origin = sprite_list[randint(0, len(sprite_list) - 1)]
        for index in range(30):
            projectile = sprites.create_projectile(img("""
                    1
                """),
                randint(-100, 100),
                randint(-100, 100),
                SpriteKind.player,
                origin)
            origin.set_flag(SpriteFlag.GHOST, True)
            projectile.image.fill(randint(1, 14))
        origin.destroy()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

projectile = None
sprite_list = []
for i in range(100):
    firework = sprites.create(img("""
            1 1 1
            1 2 1
            1 1 1
        """),
        SpriteKind.Firework)
    firework.set_position(randint(0, scene.screen_width()), randint(0, scene.screen_height()))
    firework.set_flag(SpriteFlag.GHOST, True)
```

## Tracking Single and Multiple Sprites

It is fairly common to want sprites to follow other sprites; for example, enemy sprites that want to damage the player, or faithful ally accompanying the player on an adventure.

We can implement this behavior easily using logic blocks in an on game update event.

### Project #1: Tracking with a Single Sprite and All Sprites of A Kind

1. Create a new project called `lists-its-following`
2. Create the sample code and run the code

```python
my_sprite = sprites.create(img("""
        1 . . . 1
        1 . . . 1
        . . . . .
        . . . . .
        1 . . . 1
        . 1 1 1 .
    """),
    SpriteKind.player)
controller.move_sprite(my_sprite, 100, 100)
enemy = sprites.create(img("""
        2 . . 2
        . . . .
        . 2 2 .
        2 . . 2
    """),
    SpriteKind.enemy)
enemy.x += randint(-40, 40)
enemy.y += randint(-40, 40)

def on_on_update():
    if my_sprite.x > enemy.x:
        enemy.vx = 2
    else:
        enemy.vx = -2
    if my_sprite.y > enemy.y:
        enemy.vy = 2
    else:
        enemy.vy = -2
game.on_update(on_on_update)
```

Notice the velocity. It remains constant at 2. We can write this a bit differently. We can increase the speed the further away the enemy sprite is from the player.

In the code below, we would delete all of the `if-else` statements inside of the `on_on_update()` function and replace them with the code below.
```python
if enemy.x != my_sprite.x:
    enemy.vx = my_sprite.x - enemy.x

if enemy.y != my_sprite.y:
    enemy.vy =my_sprite.y - enemy.y


```

This is also a great occasion to use lists - that way, we can have more than a single enemy follow the player.

Go onto the next challenge and add that code to this project.

### Project #2: All Sprites of Kind

Continue using the code above.

1. Add a `for n in range()` loop that creates 20 enemies in random positions on the screen.
2. In the on game update event function (`def on_on_update():`), create a new list of `sprites.all_of_kind(SpriteKind.Enemy)` to get all of the `Enemies`.
3. Use a `for-in` loop on the list to make all the enemies follow the player, not just the last one that was created.
4. Challenge: add an on overlap event between two enemies, that moves both enemies between -2 and 2 pixels in both directions, so that the enemies no longer stack on top of each other

#### Limiting Powerups

Power ups should feel like special bonuses, but they show up randomly - in some cases, you might even end up with three or four on the screen at the same time!

To address this, we can limit the number of PowerUps that are on the screen at once. When a PowerUp Sprite would be
 created, instead get an array of all existing sprites of kind PowerUp. If the length of that array is less than 2, create a PowerUp like normal. Otherwise, do not create a PowerUp Sprite.

With this, you will avoid creating new PowerUps when there are too many on the screen. This brings up an extra option for customizing your game, as well - you can increase the rate at which PowerUps are created without making the game too easy, which provides a benefit for gathering PowerUps as quickly as possible - the faster they are gathered, the faster more will come.