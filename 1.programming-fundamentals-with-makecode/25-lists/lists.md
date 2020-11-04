---
title: 'Lists'
author: 'MJ Linane'
date: '11-04-2020'
---

## Overview

Python, like all programming languages, offers us the ability to create a list. These are sometimes called an *array* in other languages. It is the perfect tool for sorting and sorting sequences of data.

## Syntax

```python
import random
# CREATING A LIST
mixed_list = ['names', 10, ['another list', 'of stuff']]

favorites = ["pie", "dogs", "computers"]

not_favorites = ["cats", "teaching history"]

# PRINT A LIST
x = favorites

# GET LENGTH OF THE LIST
x = len(favorites)

# REMOVE ITEM OFF OF THE LIST AT INDEX POSITION
x = favorites[2]

# REMOVE RANDOM ITEM FROM THE LIST -- KNOW LIST LENGTH
x = favorites[random.randint(0, 2)]

# REMOVE RANDOM ITEM FROM THE LIST -- DON'T KNOW LIST LENGTH
'''
get length of the list and -1 because the index position will always be 1 less than the total number of items in the list
'''
x = favorites[random.randint(0, len(favorites)-1)]
print(x)

# ADD ITEMS TO THE END OF THE LIST
favorites.append("mj linane")
x = favorites

# REMOVING ITEMS FROM THE LIST AT INDEX POSITION
del favorites[0]

x = favorites

# REMOVING LAST ITEM FROM THE LIST
favorites.pop()

# COMBINING LISTS
x = favorites = ["pie", "dogs", "computers"] + ["cats", "teaching history"]

# or using the + operator on the variables
x = favorites + not_favorites
#or
x = favorites += not_favorites

# CHECK FOR COMMON ITEMS IN 2 LISTS
x = any(item in favorites for item in not_favorites)
if x == True:
    print("True")
else:
    print("False")

# CHECK TO SEE IF ITEM IS IN THE LIST
if 3 in favorites:
    print('its there!')

# TO PERFORM AN ACTION ON EACH ITEM IN THE LIST
for item in favorites:
    print(item)

# SORT A LIST
print(favorites.sort())
```

## Project #1: lists_adventurer_backpack

1. Create a new project and call it `lists_adventurer_backpack`
2. Review the sample code below on how to create lists.
3. Use elements of the sample code below to create your game.

```python

# Adventurer's Backpack

# Create A List
backpack = ["sword", "helmet", "food", "healing potion", "coins"]

# Find Length List
print(len(backpack))

# Test if Item Is In Backpack
life = 20
if "mana potion" in backpack:
  print("I am healed!")
else:
  life -= 2
  print(life)

# Indexing List

# -3    -2    -1
["a", "b", "c"]
  # 0    1    2

# Find an Item At An Index Position
print(backpack[-1])

# Find Multiple Items Using Slice
# |"a"| "b"| "c"|

start = 1
finish = 3
print(backpack[start:finish])

# Remove an Item
del backpack[0]

# Remove Multiple Items
del backpack[0:2]

# Add A New Item

backpack.append("bread")

# Concatenate Lists
additional = ["armor", "shoes"]
backpack += additional

# Redefine Items At Index Positions
backpack[0] = "healing potions"

print(backpack)
```

### Game Requirements

1. Create a player sprite and give them movement controls.
2. Add at least 5 different *pickup SpriteKind* sprites appear on the screen.
3. Make one of the *pickup* sprites be health potion.
4. Add code that allows the players to add the *pickup* sprites to their inventory if they collide with them.
5. Add a sprite that will remove player health if they run into it. This could be an object, like a sword or thorns. Or it could be a part of the map, like lava.
6. Give the player the ability to add 1 life back to their life if they press a button to consume a health potion.
7. Add `if` statements that checks if they have a health potion in their inventory and that they are not at full health. Otherwise let them use the potion to add one health. The logic for this is below.

```code
if have health potion
    if health already full
       say you are already at full health
    else
        add 1 health
        delete potion
else
  say you don't have a potion
```

### Optional Challenges

1. Make the 5 items randomly placed
2. Make 4 of the items be randomly selected from a list of sprite options every time the game is loaded. (With the exception of the food/potion)

## Resources

[Further Reading](https://www.programiz.com/python-programming/list)