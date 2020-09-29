---
title: 'Makecode Info Card vs Variables'
author: 'MJ Linane'
date: '09-29-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-programming'
lesson number: ''
---

## Topic: Info Category Variable Properties

We have previously worked with variables we created. A lot of the time, software developers need to interact with variables and values that were created elsewhere.

The `info:info` category in blocks contains a few variables (data properties) which we are allowed to update. These properties have to do with score, life, and time. We will take a quick look at how to use these as variables in our code.

In this activity, you are introduced to:

- Using the `info:score` and `info:life` properties
- Combining numeric values with math operators (*)
- The benefits of using `info:score` and `info:life` over other options
- The `info:countdown` block/code
- The `loops:pause` block/code

## Topic: Using `info:score` to keep track of button presses

The first example will be a simple one - simply counting the number of buttons pressed and keeping track of them as a score. We will discuss the ability to accept any button press input:

```python
def on_button_pressed():
    # Code goes here
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)
```

We will discuss this in more detail later, but for now we just need to know that whatever is below `on_button_pressed()` will happen each time a button (`controller:A`, `controller:up`, and so on) is pressed.

### Project #1: Counting button presses

1. Review the code below
2. Create a new project and name it “button count”
3. Create the sample code and run the code

```python
# Counting Button Presses
def on_a_pressed():
    info.change_score_by(1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
```

Notice that the score pops up in the top right corner as soon as it is used for the first time - that is one benefit of using the `info.score()` function to keep track of the points the player has earned. Next, we will add in code to in order to create a timer, to see some of the other benefits of the `info` code.

### Student Task #1: 10 second button smash

1. Start with the code saved as "button count" in the prior example
2. Add in a `info.start_countdown(10)`
3. Run the code you created in task #1 a few times, and try to get different scores. Notice the benefits of using both the `info.start_countdown(10)` and the `info.change_score_by(1)` - the countdown creates a timer that counts down to 0, and then ends the game at that point. The score keeps track of the value for you which is shown in the top right corner. When the game is over, the `info.score()` maintains a `info.high_score()` automatically through multiple runs of the game.

## Topic: Using `info:life`

Beyond score, another important value to keep track of is the players life total. This allows us to make games where players can be penalized for mistakes, without simply ending the game immediately when they make one.

### Project #2: changing `info.life()` totals

1. Review the code below
2. Create a new project and name it “do not touch the button”
3. Create the sample code and run the code

```python
def on_a_pressed():
    info.change_life_by(-1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

info.set_life(1)
```

This simple game gives the user a simple task - to not touch a button. If they do touch a button, the life will go down to 0, and they will lose. The game is a bit boring, but it does demonstrate a few of the benefits of using `info.life()`: life total shows up in the corner as a number of hearts, and when you run out of the lives, the game will end.

### Student Task #2: Touch the button 15 times

1. Start with the code saved as "do not touch the button" in the prior example.
2. Modify the initial value of the life to be 15, instead of just 1.
3. Add in the `info.change_score_by()` code used in the first task, and modify it to add 2 to the score each time a button is pressed.
4. Add in a `info.start_countdown()`, and set it to run out after 2 seconds

### Student Task #3: Estimate rate of presses

When a nurse needs to take a patient's heart rate with their other vital signs, they do not want to (or have time to) sit around for a full minute to count how many beats there are. Instead, they can use another, quicker approach to estimate the patient's heart rate - count how many heart beats there are over 15 seconds, and then multiply that value by 4 to get an estimate for the full minute. In this task, we will use the score to do the same thing, only with button presses. The `pause()` code is new in this example, and pauses the code at that point for however many milliseconds it is asked to wait - in this case, we pass 6000 ms so that it pauses for 6 seconds, and then multiply by 10 to get an estimate for the full 60 seconds (one minute).

#### Setup The Code

1. Review the code below
2. Create a new project and name it “button rate”
3. Create and run the code

```python
def on_a_pressed():
    info.change_score_by(1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

my_sprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . d d d d d d . . . . .
        . . . . d d d d d d d d . . . .
        . . . . d d f d d f d d . . . .
        . . . . d d d d d d d d . . . .
        . . . . d d f d d f d d . . . .
        . . . . d d d f f d d d . . . .
        . . . . . d d d d d d . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
my_sprite.set_position(25, 60)
game.splash("Press buttons for 6 seconds!")
pause(6000)
my_sprite.say(":)")
```

### Modify The Code

1. Change the `my_sprite.say()` code so that after 6 seconds have passed it says the `info.score()`. You may also want it to show a message explaining what the value represents
   1. Review the Variable Math activity if you're having trouble making the sprite say the `info.score()` - it is stored as a number.
2. Use the `*` to multiply the `info.score()` by 10 and store it in a variable called `minute_score`, so it will correspond to one minute's worth of button presses.
3. Make the sprite say the result stored in `minute_score`: `my_sprite.say(minute_score)`. Edit the sprite so it looks better.

#### Challenge

Instead of outputting an exact estimate, give a range that the button presses will likely fall into - estimate this by making the low end of the range correspond to (score - 1) * 10, and the high end of the range correspond to (score + 1) * 10. For example, if the score were 5, the output should be something along the lines of "between 40 and 60".

#### Hint

When doing the challenge, remember to pay careful attention to the order of operations and parentheses (Python) to get the right equation.

To join more than just two strings and numbers, press the + to add more locations to combine strings

```python
my_sprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . 6 6 6 6 6 6 6 6 6 6 6 . . .
        . . 6 . . . . . . . . . 6 . . .
        . . 6 . 6 6 . . . 6 6 . 6 . . .
        . . 6 . . . . . . . . . 6 . . .
        . . 6 . . . . . . . . . 6 . . .
        . . 6 . 6 . . . . 6 6 . 6 . . .
        . . 6 . 6 6 6 6 6 6 . . 6 . . .
        . . 6 . . . . . . . . . 6 . . .
        . . 6 6 6 6 6 6 6 6 6 6 6 . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
my_sprite.say("score " + "is " + "here")
```

## What We Learned

- List one extra behavior you get for each of the three values we used in the `info:info` category (`info.score()`, `info.lives()`, and `info.start_countdown()`).
- List one potential downside of using `info.score()` over just using your own variables to keep track of the state of your game.
- Consider what you would do if you needed to keep track of the number of coins the player has earned, the number of keys they have collected, and the number of chicken legs they have to eat. Consider whether using `info.score()` be helpful in storing all these values.
