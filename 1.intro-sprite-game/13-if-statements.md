---
title: 'Logic: If-Else'
author: 'MJ Linane'
date: '10-13-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview of Logic - True and False

Logic in software development allows for flexible programs that respond appropriately to different conditions. In this section, we will identify how comparisons can be used within our code.

In Python, logic allows for games that react to user input and the state of the game. A boolean value can be stored as a variable in Python: `True` or `False`.

```python
is_teacher = True;
```

## Concept: Logical comparison

Comparison logic with the `if-else` statement

In our games we will often want to compare values and take an action when the comparison statement is true.

> Example: Is my_value (3) smaller than a test_value (5)? If it is `True` that myValue is smaller than the testValue, then we will add 1 to myValue.

We perform comparison tests with and `if-else` statement.

We have already seen similar behaviors in events like `on_on_overlap`. **If** the two sprites were overlapping and not ghosts, then the code for the event will run (for example, the score might increase).

`if` statements allow us to program a behavior based on the state of the game.

## Concept: `if-else` Statement

`if-else` statements perform a test, and if the test evaluates to true, then it will run code that is given. Some further examples are:

* if the score is greater than 10, then give additional countdown time
* if the player has 0 lives left, then game over

These are what are known as comparisons because they compare the value of two things.

To use an `if-else` statement, we must fill it with a comparison test. If the test is true the code in the block will run. Below is a comparison to see if high score is greater than 5.

```python
if info.score() > 5:
    game.splash("Good luck!")
```

## Concept: Comparison Operators

When we make comparisons, we have two numbers, in a specific order, and what is know as a comparison operator. A comparison operator allows us to specify what type of comparison we are doing. Some basic ones are:

* Equals: `a == b`
* Not Equals: `a != b`
* Less than: `a < b`
* Less than or equal to: `a <= b`
* Greater than: `a > b`
* Greater than or equal to: `a >= b`

We would add these inside of the parenthesis of the if-else condition:

```python
a = 2
b = 2

if a==b:
    game.splash("equal")
```

In the example above, this would print the statement because that condition check, `==`, is equal to `True`.

## Example #1: Less than

1. Play the game linked below
2. Review the code that uses comparisons
3. Look at how it uses if logic and a less than comparison to modify the game

[Example Code](https://arcade.makecode.com/73705-28946-93201-18267)

When the game creates a new enemy, it checks to see if the player’s score is less than a certain value.

If that is the case, the player has just started playing the game, so the game makes it easier for the player by decreasing the speed in which the projectiles are thrown at the player.

## Example #2: Scoring

1. Play the game linked above
2. Review the code that uses comparisons
3. Look at how it uses if logic and a greater than comparison to modify the game

[Example Code](https://arcade.makecode.com/09108-15465-13167-28402)

When the player collects a cherry, if the player has collected more than 5, then the sprite says “Too many cherries”.

## Example #3: Equality

1. Play the game linked above
2. Review the code that uses comparisons
3. Look at how it uses if logic and an equality comparison to modify the game

[Example Code]([https://link](https://makecode.com/_3pgH9LA5kL9b))

## Example #4: Sequential (Multiple) If Statements

1. Play the game linked below
2. Review the code that uses comparisons
3. Look at how it uses if logic and multiple comparisons to modify the game

[Example Code](https://makecode.com/_FhqaRpe6Riau)

With Python, we are allowed to ask a series of `if` questions. If any are equal to `True` the program will immediately execute that code. Once that code has completed, the program will move on to the next `if` statement, evaluate, and either execute the code or move on to the next line.

If any statement is equal to `False`, then the code indented under that `if` statement, will be skipped.

## Project 1: scoring_if (if)

1. Create a new project called `scoring_if`
2. Create a Sprite
3. When the player presses the A button, increase the score by 1
4. When the player presses the B button, if the player’s score is less than 10, make the Sprite say something

## Project 2: follow_me (if)

1. Start a new project called `follow_me`
2. Create 2 sprites, a leader and a follower
3. Set the x position of the leader at a random value between 100 and 140 and set the x position of the follower at 20.
4. Make it so that when the player presses the A button, if the leader’s x position is greater than the follower’s, then make the follower change their x position by 10

## Project 3: equal_and_greater_than (multiple ifs)

1. Create a new project called `equal_and_greater_than`
2. Create a sprite
3. Make it so that when the player presses the A button, the score increases by 1
4. In this event, if the player’s score is above 10, make the sprite congratulate the player on their high score
5. In the same event, if the player’s score is an even number, change the background to a random color

### Project 3 Optional Challenges

1. Add projectiles that fire from the sprite when the score is increased to a value greater than 5
2. If the score reaches 20, change the sprite‘s image
