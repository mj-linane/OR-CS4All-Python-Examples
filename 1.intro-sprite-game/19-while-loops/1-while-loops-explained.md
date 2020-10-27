---
title: 'While Loops Explained'
author: 'MJ Linane'
date: '10-27-2020'
---

## Overview

When writing code, we want to tell the computer to do something over and over again. This is called a **loop**. In programming, there are 2 different types of loops.

* indefinite iteration: number of times isn't specified in advance.
* definite iteration: specific number of times.

## While Loop Syntax

### Example #1 - Simple Loop

Anything indented under the while loop will continue to run until the initial condition is met.

```text
while <expression>:
  <statement(s)>
```

```python
a = 1
while a != 0:
  print("not yet!")
```

Here, the code will continually print out "not yet!" *until* the condition `a` equals `0`. When `a=0`, the code will stop and the next line of code will execute.

#### Simple Loop Practical Example - Dice Roller

Try out the following code in Repl.it.

```python
import random
min = 1
max = 6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Roll the dices again?")
```

### Example #2 - Infinite Loop

Here we see what happens when we have code that is placed after a while loop.

```text
while <expression>:
  <statement(s)>
<statements(s)>
```

```python
a = 1
while a != 0:
  print("not yet!")
print("won't print")
```

Here, our `while` loop never exits the loop, so the next line `print("won't print")` will never run because the loop above never ends.

#### Infinite Loop Example - Losing Battle

Try this code in Repl.it.

```python
# Losing battle
# Warning about infinite loops

print("Your hero is surrounded by the enemy")
print("You are without backup")
print("Your hero draws their sword")

health = 100
trolls = 0
damage = 7

while health > 0:
    print("Your hero has ", health, "health")
    #trolls=trolls +1
    trolls += 1
    health -= damage

    print("Your hero swings and defeats a troll, but takes",
          damage, "damage points.")

print("Your hero fought bravely and defeated", trolls, "trolls.")
print("But your hero died in battle")
```

#### Infinite Loop Example - Annoying Child

```python
# Annoying child simulator

print("I am a annoying child")

# Sentry variable // check
response = ""

while response != "Because":
  response = input("Why?")

print("oh")
```

## How To Stop A Loop With A Sentry Variable

We can stop a loop by setting up something called a "sentry variable". Like a sentry that guards a military building, our sentry will guard our program to make sure we don't accidentally create an infinite loop.

```python
# Controlling Sentry Variable // Infinite loop
counter = 0
while counter < 20:
    print(counter)

    # Added to prevent infinite loop
    counter = counter + 1
```

In the code above we first setup our sentry variable: `counter`. These often have some variable name that indicate that it is going to count up the number of times the program runs.

`counter = 0`

We then create our `while` loop condition `while counter <20:`

We then run our code as a result of that while loop being `True`:

```python
print(counter)
```

But instead of leaving it at that, we add in a bit of code to change our sentry variable every time the code runs: `counter = counter + 1`.

This will increase the value of the variable `counter` every time the program loops. This will make sure that the condition we are looking for: `counter < 20`, eventually goes past `20` and stops the while loop. The program can then proceed.

## Learn More

Want to learn more about while loops? Check out this article that goes into them with more detail.

[Full Documentation](https://realpython.com/python-while-loop/)
