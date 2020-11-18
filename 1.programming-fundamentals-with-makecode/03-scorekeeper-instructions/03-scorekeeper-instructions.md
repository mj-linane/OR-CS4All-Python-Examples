---
title: 'Lesson 4: Constants, Variables, and Scorekeeper App'
author: 'MJ Linane'
date: '09-29-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.programming-variables-math-random'
lesson number: '4'
---

## Topic 1: Constants and Variables

Computer programs process information. Some of the information that is input, stored, and used in a computer program has a value that is constant, meaning it does not change throughout the course of the program. An example of a constant in math is ‘pi’ because ‘pi’ has one value that never changes. Other pieces of information have values that vary or change during the running of a program. Programmers create variables to hold the value of information that may change. In a game program, a variable may be created to hold the player’s current score, since that value would change (hopefully!) during the course of the game.

### Discussion

- What pieces of information have values that don’t change during the course of a single day (constants)?
- What pieces of information have values that do change during the course of a single day (variables)

Constants and variables can be numbers and/or text.

### How Variables are Stored

Variables hold a specific type of information. A computer's memory can store many different type of variables. On MakeCode, we can keep track of numbers, strings(text), booleans, and sprites. The first time you use a variable, its type is assigned to match whatever it is holding.

- A number variable could hold numerical data such as the year, the temperature, or the degree of acceleration.
- A string variable holds a string of alphanumeric characters such as a person’s name, a password, or the day of the week.
- A boolean variable has only two values: true or false. You might have certain things that happen only when the variable called `game_over` is false, for example.
- A sprite is a special variable that represents a single dot on the screen and holds two separate values for the row and column the dot is currently in.

### Rock Paper Scissors

- Play a game of Rock Paper Scissors [Rock Paper Scissors Game](https://www.rpsgame.org/)
- Keep track of how many times you won and a separate number tracking the number of times you tie.
- **Play**: Play for a couple of minutes and, when done, add up your scores and how many ‘rounds’ you played.
- **Play again**: Now start over and play again for another minute. When done, add up your scores and how many ‘rounds’ you played.
- When prompted, share your results in the chat.

### CONSTANTS vs Variables

A **constant** is a saved value that does not change in the program.
A **variable** is a saved value that does change in the program.

1. List the constants in the Rock Paper Scissors Game and their type.

2. List the variables in the Rock Paper Scissors Game and their type.

### Coding Constants and Variables

Notice here that the “ADDRESS” is capitalized. This indicates that it is a constant and should not be changed in the program. However, there is nothing in Python that will absolutely stop a programmer from redefining that value.

## Topic 2: Coding A Score Keeper Overview

You will be creating a program that will act as a scorekeeper for the Rock Paper Scissors game. They will need to create variables for the parts of scorekeeper that change over the course of a gaming session. What are those variables?

- The number of times the first player wins
- The number of times the second player wins
- The number of times the players tie

### Step 1: Creating and naming variables

Let's work together on creating some variable names.

What would be a unique and clear name for the variable that will keep track of the number of times Player A wins?

### Step 2: Initialize Your Variables

In MakeCode, from the Variables menu, make and name these three variables: `player_a_wins`, `player_b_wins`, `player_ties`.

It is important to give your variables an initial value. The initial value is the value the variable will hold each time the program starts. For our scorekeeper program, we will give each variable the value 0 (zero) at the start of the program.

```python
player_a_wins = 0
player_b_wins = 0
player_ties = 0
```

### Step 3: Updating the variable value

In our program, we want to keep track of the number of times each player wins and the number of times they tie. We can use the buttons A and B to do this.

> Pseudocode:
> Press button A to record a win for player A
> Press button B to record a win for player B
> Press button “up” to record a tie

We already initialized these variables and now need to code to update the values at each round of the game.

- Each time the scorekeeper presses button A to record a win for Player A, we want to add 1 to the current value of the variable `player_a_wins`.
- Each time the scorekeeper presses button B, to record a win for Player B, we want to add 1 to the current value of the variable `player_b_wins`.
- Each time the scorekeeper presses both button A and button B at the same time to record a tie, we want to add 1 to the current value of the variable `player_ties`.

Add the event listeners with the following code:

```python
player_a_wins = 0
player_b_wins = 0
player_ties = 0
def on_a_pressed():
    global player_a_wins

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global player_b_wins

controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_up_pressed():
    global player_ties

controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)
```

### Step 4: Change variable

Add code to each of the `on_pressed()` to increase the number of wins for each player.

```python
player_a_wins = 0
player_b_wins = 0
player_ties = 0

def on_a_pressed():
    global player_a_wins
    player_a_wins = player_a_wins + 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global player_b_wins
    player_b_wins = player_2_wins + 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_up_pressed():
    global player_ties
    player_ties = player_ties + 1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)
```

### Step 5: User feedback

Whenever the scorekeeper presses button A, button B, or both buttons together, we will give the user visual feedback acknowledging that the user pressed a button. We can do this by coding our program to display a splash message:

- a "player A scored" each time the user presses button A to record a win for Player A,
- a "player B scored" for each time the user presses button ‘B’ to record a win for Player B,
- a "tie" for each time the user presses both button A and button B together to record a tie.

We add these messages within each button press function.

```python
game.splash("player A scored")
```

### Step 6: Showing Total Number of Rounds Played and Scores

There is more we can do with the input we received using this program. We can use mathematical operations on our variables.

Example: Perhaps you’d like to keep track of, and show the player the total number of ‘rounds’ that were played. To do this, we can add the values stored in the variables we created to keep track of how many times each player won and how many times they tied.

First, display a string to show the player that the following sum represents the total number of rounds played.

Our program will add the values stored in the variables player_a_wins, player_b_wins, and player_ties and then display the sum of this mathematical operation.

The blocks for the mathematical operations adding, subtracting, multiplying, and dividing are listed in the Math section of the Toolbox.

Replace the default values of zero with the names of the variables we want to add together.
Notice that because we are adding three variables together we need a second math block. First we add the values for player_a_wins and player_b_wins, then add player_ties.

Notice, we need to add in the `\n`, this will put the text on the new line. We also use the `game.show_long_text()` to show the entire text on the screen.

```python
def on_down_pressed():
    game.show_long_text("Rounds played: " + (str((player_a_wins + player_b_wins + player_ties)) + "\n Player A Score: " + str(player_a_wins) + "\n Player B Score: " + str(player_b_wins)),
        DialogLayout.BOTTOM)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)
```

Test the program again to make sure that it runs correctly and displays the correct numbers for each variable.

What other math operations could provide valuable information from the values stored in these variables?

### Step 7: Additional Challenges

1. Calculate and display a player’s wins and/or losses as a percentage of all rounds played.
2. Calculate a display the number of tied games as a percentage of all rounds played.
3. Change the background color for each player when they score. Example is when player A scores, background is purple, but when player B scores, background is red.
4. Add a sprite that shows up when a player scores, like a fireworks or a star.
5. Show each of the player's scores when they win.

## Submit

1. Publish your code
2. Submit the link to Google Classroom
