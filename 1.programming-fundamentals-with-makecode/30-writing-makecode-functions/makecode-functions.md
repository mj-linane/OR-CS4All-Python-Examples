---
title: Writing Make Code Functions
course: CS4ALL
---
## Writing Functions

### Example: Setting Up the Level
```python
def setup_level():
    info.lives(5)
    info.score(0)
```

### Example: Creating Starting Enemies
```python
def create_enemies():
    for n in range(10):
        new_enemy = sprites.create(img("""
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
"""), SpriteKind.Enemy)
        x_range = randint(0, scene.screen_width())
        y_range = randint(0, scene.screen_height())
        new_enemy.set_position(x_range, y_range)
```

## Writing Functions With Parameters

The following are examples of ways to use organize your code around functions and parameters.

### Example: Setting up a level

```python
def setup_level(lives_input, score_input):
    info.lives(lives_input)
    info.score(score_input)
```

### Example: Choosing things
```python
def choose_for_me(choice1, choice2):
    if Math.percent_chance(50): # Math.percent_chance() is a Makecode method
        print("I think " + choice1 + " is the better choice")
    else:
        print("I think " + choice2 + " is the better choice")

# Use
choose_for_me("coffee", "tea")
choose_for_me("dogs", "cats")
```

### Example: Update numbers
```python
def change_by_five(value: int, add: bool):
    if add == True:
        value+=5
    else:
        value -= 5
    game.splash("" + value)

# Run the code
change_by_five(2, True)
change_by_five(5, False)
```

### Example: Move Sprites When A Condition Is True

```python
def horizontal_movement(player: str, left: bool):
    if left == True:
        player.x -= 10
    else:
        player.x += 10
```

## Writing Functions with Return Values

### Example: Give me 5 - Setting a value to a variable
```python
def give_me_five():
    return 5

# Call and set to a variable
returned_value = give_me_five()
```
### Example: Who Are You?
```python
def a_name(name):
    return name

# Call the function
game.splash(a_name("MJ"))
```

### Example: Absolute Value

```python
def make_positive(number):
    if number < 0:
        return -1 * number
    else:
        return number

# Call the function
pos_number = make_positive(-3)
```

### Example: Finding Tree

```python
def contains_three(min_num, max_num):
   for n in range(min_num, max_num):
      if n == 3:
         return True
   return False

# Call the function
found = contains_three(0,5)
game.splash(found)
found = contains_three(5,10)
game.splash(found)
```

`contains_three()` will go through all values starting at `min_num` and ending at `max_num`, logging the value of each until it finds the value `3`. If it finds `3`, it will return `True`; otherwise, it will return `False`.

In the first case shown in the code, `contains_three(0, 5)`, the function only logs 0, 1, 2, and 3 because the function stopped once it found `3` and returned `True`.

In the second case shown in the code `contains_three(5, 10)`, the function logs all values between 5 and 10 because it never finds `3`, and returns `False`.

### Practice Return Values

1. Create a function named addOrRemove 
2. Add two parameters to the function: input of type number, and up of type 
   boolean
3. Add an if ... else to the function
4. if up is true, return input plus one 
5. otherwise, return input minus one


## Common Errors When Writing Return Statements

### Error #1: Returning Too Early

In the following snippet, the intention of hello is to return the value 5, and also splash “5 is returned!”.

```python
def hello():
    output = 5
    return output

    game.splash(output + "is returned!")
```

However, because the return statement comes before the splash,

the function ends before the value is splashed. This can be fixed in this case by switching the order of the statements, so that the return value is at the end of the function.

```python
def hello():
    output = 5
    game.splash(output + "is returned!")
    
    return output

```

### Error #2 Missing a Return

In this example, the intention is to return 5 half the time, and otherwise return 10.

```python
def world():
    if Math.percent_chance(50):
        return 5
    elif Math.percent_chance(50):
        return 10 
```

This code can be fixed by removing the condition on the else as follows:

```python
def world():
    if Math.percent_chance(50):
        return 5
    else:
        return 10 
```

Another way to address this issue is to only have a single return statement, and create an `output` variable to 
return. For example, the above code could be rewritten as the following:

```python
def world():
    output = 0
    if Math.percent_chance(50):
        output = 5
    else:
        output = 10
        
    return output
```