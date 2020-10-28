---
title: 'Sprites Variables, and Math'
author: 'MJ Linane'
date: '09-22-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\03.variables'
lesson number: ''
---

## Part 1: Sprites

Games tell a story, and those stories require characters. In MakeCode Arcade, those characters are generally represented using sprites. This activity equips students with the skills necessary to create, test and save sprites using the MakeCode development environment. Students will build unique sprites by using the sprite menu and the integrated image editor.

The `my_sprite = sprites.create()` is the code that we will discuss. The following example shows the creation of a sprite with a blank image:

```python
my_sprite = sprites.create(img`
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
`, SpriteKind.Player)
```

Clicking on the image icon will bring up the Image Editor, allowing you to draw an image for your own sprite.

### Example #1: Sprites

Look at the variables and note that a name for the sprite is `my_sprite`. It is set to an image for the sprite (it's hot sauce!).

```python
my_sprite = sprites.create(img`
. . . . . . . . . . . . . . . .
. . . . . . . . 2 . . . . . . .
. . . . . . . 7 7 7 . . . . . .
. . . . . . . 7 7 7 . . . . . .
. . . . . . 2 2 2 2 2 . . . . .
. . . . . 2 2 2 1 2 2 2 . . . .
. . . . . 2 1 2 2 1 2 2 . . . .
. . . . . 2 2 7 7 2 2 2 . . . .
. . . . . 2 7 2 7 2 2 2 . . . .
. . . . . 2 2 2 2 7 2 2 . . . .
. . . . . 2 2 2 7 7 2 2 . . . .
. . . . . 2 1 2 2 2 2 2 . . . .
. . . . . 2 2 1 1 2 2 2 . . . .
. . . . . 2 2 2 2 1 2 2 . . . .
. . . . . 2 2 2 2 2 2 2 . . . .
. . . . . 2 2 2 2 2 2 2 . . . .
`, SpriteKind.Player)
```

### Project #1: Create your own sprite

Create a new project on MakeCode Arcade

1. Create a new sprite
2. The default sprite is 16x16 pixels - press the change sprite size button to make a sprite that is 32x32 pixels
3. Draw a unique sprite
4. Pixel dimensions: when using the image editor, the pixel dimensions are displayed in the lower left corner. The width is the first number and the height is the second number.

### Project #2: Build a "rainbow numbers" sprite that uses every color in the editor

1. Make a blank 32x32 sprite
2. Hover over every color and find color index 0 and add that color on the far left
3. Then find and add the other colors in the shape of their corresponding code index number
4. Arrange them inside the Sprite Editor workspace so you have all 15 index colors
5. Look at how the sprite image is represented in Python

#### Optional Challenge

Try changing the background color using `scene.set_background_color()`. You will need to pass in a number as a parameter into the `set_background_color()` that is the same as the color you want. For example, `scene.set_background_color(0)` would give me a black background.

## Part 2 Variables

**Variables**: a container used to store values in your code.

A variable points to a container that can store data. We have previously used variable names for sprites (for example, `my_sprite`). Variables act like an address, and allow us to store, retrieve, and update data.

For example, the variable `my_sprite` allowed us to interact with the sprite in our game. The word "variable" also means change. We can update the values our variable point to, such as updating the `my_sprite` variable to point to a completely different sprite.

Variables are used extensively in code. Variables allow code to be written in a generic way, and allow for easier reuse of our code. Math equations, like `x = 2y`, provide familiar examples in the use of variables that apply to code by assigning known values to variables to calculate unknown variable values.

If we know `y = 3` we can calculate `x` from our equation. Later on, `y` can have a different value, like `Y = 7`. We can reuse the equation,`x = 2y`, for both values of `y`. This way, the value of `x` will change alongside the value of `Y`.

## Concept 1: Types of Variables

1. String
2. Integer

```python
name = "mj" # string
age = 35

game.splash(name)
game.splash(age)
```

## Concept 2: Assign Number Variables and displaying numeric values as strings

Here we are setting 2 the two variables, `x` and `y`, to values `1` and `2`. When we go to show them in the game, we need to use `str()`. This is a built in Python method that will convert whatever is inside of it to a string. Here, `game.splash()` requires strings as parameters. If we tried to call `game.splash()` with `game.splash(1,2)` Python is going to complain. Instead we need to wrap our numbers with `str()` to convert them to a string.

```python
x = 1
y = 2
game.splash(str(1) + str(2))
```

## Concept 3: Using Math Operators with Variables

### Example #1: Math equation in a variable

1. Create a new project and name it `equation_variable`
2. Create the sample code and run the code

Here set `answer` to get the result of `3+5`.

```python
answer = 0
answer = 3 + 5
game.splash("3 + 5 = " + answer)
```

### Student Task #1: Try new values in the equation

1. Starting with example #1
2. Experiment using different numbers in our equation (e.g. 9 + 2)
3. Test at least 3 different equations
4. Challenge: make longer addition equations with `math` blocks so that the code calculates the sum of 5 or more numbers. If the equation gets too long, then display using `game.show_long_text()`

The splash screen is primarily designed for short sentences. This limits the length of equation we can effectively display. `game.show_long_text()` allows for a better representation for longer text.

## Concept: Basic math operators with variables

We can convert variable based math equations, like A = B + C, into code using our code variables and math operators.

### Operators

In Python, the following order of operation precedence applies:

1. Multiplication (*) and Division (/)
2. Addition (+) and Subtraction (-)

Note: Python uses the* symbol for multiplication the / for division. In order to change order of these operations, you can use parentheses ( ) around expressions just like in math.

### Example #2: Displaying expressions with game.splash()

- Review the code below
- Create the sample code and run the code
- Press the A button to see the second equation on splash message

```python
answer = 0
first_number = 0
second_number = 0

first_number = 15
second_number = 5
answer = first_number - second_number
game.splash("15 - 5 = " + answer)

first_number = 5
second_number = 7
answer = first_number * second_number
game.splash("5 * 7 = " + answer)
```

### Student Task #2: Basic math operators with variables

1. Start with example #2
2. Create a new variable called `third_number` and assign it the result of a math equation using both the addition operator (+) and the multiplication operator (*)
3. Create a new variable called `forth_number` and assign it the result of a math equation using 3 different operators

#### Optional Challenge Math Operators

Create an equation that:

- uses all 4 basic operators (+, -, *, /)
- uses at least 5 unique variables

### Student Task #4: Movement

### Student Task #5: Conversion

1. Create 2 variables
   1. `temp_c` (temperature Celsius)
   2. `temp_c` (temperature Fahrenheit)
2. Initialize `temp_c` with common Celsius temperature (for example, 22.0)
3. Create an equation using the formula:
   1. `temp_f = temp_c × 9/5 + 32` and assign it to a new variable `temp`
4. Show the `temp` in a Splash Screen
5. Challenge: create an equation for converting back to Celsius:
    1. `temp_c = (temp_f - 32) × 5/9`
    2. pay careful attention to the parentheses

### Student Task #5: Debugging

We decided that we want to have three different variables in our code - `a`, `b`, and `c`. The variable `a` should be set to 3, `b` should be set to `a + 5`, and `c` should be set to `a + 2 * b`. This should result in `a` storing 3, `b` storing 8, and `c` storing 19 at the end. When we wrote this out, though, we found that we couldn't run our code. What is going wrong in the following code, and how can you fix it?


After you are able to run the code, the value of `c` should be shown on the screen. There's a problem because the value shown is not quite right. Rearrange the existing blocks so that it produces the correct output, without removing or adding any JavaScript or blocks beyond what was necessary for part 1. What went wrong? Fix the output.

## Variables Summary

Variables are names that point to a container that can be updated to hold different data types.
Data Types used in variables so far are `Sprite`, `numbers` and `strings`.

**Strings** are sequences of characters (like the letters found on a keyboard) surrounded by quotation marks.

Displaying a number often requires type coercion by using `text:join` to convert a number into a string.

## Additional Resources

(Python Scope of Variables (article) - DataCamp)[https://www.datacamp.com/community/tutorials/scope-of-variables-python]
