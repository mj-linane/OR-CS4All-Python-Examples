---
title: 'If-Else Statements'
author: 'MJ Linane'
date: '10-13-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Overview if-else Statements

In our games we will often want to compare values, and take an action based on the result of the comparison.

> Example: Is my value smaller than a test value? If it is true that my value (3) is smaller than the test value (5) then we will add to my value. Otherwise, we will subtract from the value.

Examples of if-else statments in games:

* if player score is greater than the enemy score, then we gain points on overlap
* if the player has 0 lives left, then we set to game over
* if we have the secret key, then we can enter the room.

## Concept: if-else statement

We have seen in the previous lesson if statements perform a test and if the logic test evaluates to true, then it will run code that is given.

```python
life = 5
if life > 2:
  game.splash("3 or more lives")
```

### Adding an `else` statement

When we use an if statement, we have the option to add an else statement. An else code will only run in the event that the logic test given evaluates to false. In other words, if the test is true, then the if's code will run, else, the else code will run.

```python
high_score = 0

if high_score > 5:
  game.splash("good luck!")

else:
  game.splash("set high score")
```

## Concept: `if else` statement

Using `if-else` allows us to split all comparisons into two categories - either the comparison is true or false (not true).

What if we needed to split a comparison into three or four categories?

We can use the else if's to add additional comparisons.

Python lets us create additional condition checks. This is kind of like asking a multiple choice question. It allows for another logic test that splits the cases after the original logic test evaluates to false.

We can compare the score with 3 possible results.

For example, consider the case where we want to split scores into three groups: beginner, intermediate, and expert.

* if score greater than 100 “you are an expert”
* or else if greater than 50 “you are intermediate”
* or else, “you are a beginner”

```python
if score > 100:
  game.splash("you are an expert")
elif score > 50:
  game.splash("you are intermediate")
else:
  game.splash("you are a beginner")
```

This code will first check if the high score for the game is greater than 100. If it is, then it will identify the player is an “expert” and skip the rest of the comparison tests.

If it is not greater than 100, then the second logic test is run to see if the score is greater than 50. If it is, then it will identify the player as “intermediate.”

If it is not greater than 50, it will run the else section and rank the player a “beginner.”

## Example: random_message

For each example below,

1. Play the game
2. Review the code that uses comparisons
3. Identify how the behavior is different from the other examples

### Example #1a: Random Message

[Example #1a](https://makecode.com/_HXMRAzYY4YkU)

### Example #1b: Check the Button

[Example #1b](https://makecode.com/_LigLWHR00d74)

### Example #1c: Using ``||logic:else||``

[Example #1c](https://makecode.com/_FDoAgwhKdh1X)

## Project 1: button_game (if-else if-else)

1. Start with the code from example #1c above
2. Add `else` statement in the button press events that run code when the player enters the wrong button
3. Decrease the players score by 1 when they press the wrong button
4. Now add a timer, and congratulate the player at the end of the game, giving them a specific message based on their score.
5. Create an event for when the countdown ends by defining a function called `def on_countdown_end()`
6. Check to see if the player’s score is less than 20. If it is, use `game.splash()` to say “Beginner score of “ and then the player’s score
7. Use an else statement to do the same for if the player’s score was greater than or equal to 20 but say “Pro score of “ and then the player’s score
8. Use a game over block to let the game know that it is over with `game.over()`

### Project 1 Optional Challenge

Make the sprite have a shake or bump effect each time it has a say so can see when letter updates even when it is the same as the previous time.
