---
title: 'Sprites Variables, and Math'
author: 'MJ Linane'
date: '09-22-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\03.variables'
lesson number: ''
---

[Website](https://arcade.makecode.com/courses/csintro1/intro/sprites)

## Part 1: Sprites

Games tell a story, and those stories require characters. In MakeCode Arcade, those characters are generally represented using sprites. This activity equips students with the skills necessary to create, test and save sprites using the MakeCode development environment. Students will build unique sprites by using the sprite menu and the integrated image editor.

Image Editor Features

In this activity, students are introduced to:

- Using blocks
- `sprites:Sprites` and `images:Images`
- Using the Image Editor
- Pixels and pixel Colors
- Viewing JavaScript
- Color codes in the Image Editor, Blocks, and JavaScript
- Concept: Set a `sprites:Sprite` variable to an image using the image editor
- Link to Video

The blocks needed to create sprites are found in the `sprites:Sprites` menu. The `variables:set my_sprite to` is the first block in this category that we will discuss. The following example shows the creation of a sprite with a blank image.

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

Look at the blocks, and note that a name for the sprite `my_sprite` is set to an image for the sprite (it's hot sauce!).

```python
mySprite = sprites.create(img`
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

### Student Task #1: Create your own sprite

Create a new project on MakeCode

1. Create a new sprite
2. The default sprite is 16x16 pixels - press the change sprite size button to make a sprite that is 32x32 pixels
3. Draw a unique sprite
4. Pixel dimensions: when using the image editor, the pixel dimensions are displayed in the lower left corner. The width is the first number and the height is the second number.

### Student Task #2: Build a "rainbow numbers" sprite that uses every color in the editor

1. Make a blank 32x32 sprite
2. Hover over every color and find color index 0 and add that color on the far left
3. Then find and add the other colors in the shape of their corresponding code index number
4. Arrange them inside the Sprite Editor workspace so you have all 15 index colors
5. Look at how the sprite image is represented in Python

Background color
Try changing the background color using `scene:set background color to` in the `scene:Scene` category.

~

### What We Learned

Make a table showing
Color index (1-15)
Color (use an approximate color name like white, red, pink, ...)
Color representation in JavaScript
Explain what happens to the color index 0 in JavaScript (form a hypothesis).
Explain why we see only 14 colors at a time, despite the fact that there are 16 color indexes (0-15) in the image editor.

## Part 2 Variables

**Variable**: a container used to store values in your code.

A variable points to a container that can store data. We have previously used variable names for sprites (for example, `my_sprite`). Variables act like an address, and allow us to store, retrieve, and update data.

For the examples in the "sprites" lesson, the variable `variables:mySprite` allowed us to interact with the sprite in our game. The word "variable" also means change. We can update the values our variable point to, such as updating the `variables:mySprite` variable to point to a completely different sprite.

Variables are used extensively in code. Variables allow code to be written in a generic way, and allow for easier reuse of our code. Math equations, like X = 2Y, provide familiar examples in the use of variables that apply to code by assigning known values to variables to calculate unknown variable values.

If we know Y = 3 we can calculate X from our equation. Later on, Y can have a different value, like Y = 7. We can reuse the equation, X = 2Y, for both values of Y. This way, the value of X will change alongside the value of Y.

In this activity, students are introduced to:

- Expressing numeric operations with math operators (+, -, *, /)
- Storing the result of an equation in a variable
- Evaluating equations using variables
- Modifying and creating variable equations
- Displaying text with `game:splash` by using `text:join`
- Differentiating between the number and string data types

## Concept 1: Types of Variables

1. String
2. Integer

```python
name = "mj" # string
age = 35

game.splash(name)
game.splash(age)
```

## Concept 2: Assign Number Variables and displaying numeric values

```python
x = 1
y = 2
game.splash(str(1) + str(2))
```

## Concept 3: Using Math Operators with Variables

### Example #1: Math equation in a variable #example-1

1. Create a new project and name it “equation variable”
2. Create the sample code and run the code

```python
answer = 0
answer = 3 + 5
game.splash("3 + 5 = " + answer)
```

### Student Task #1: Try new values in the equation

1. Starting with example #1
2. Experiment using different numbers in our equation (e.g. 9 + 2)
3. Test at least 3 different equations
4. Challenge: make longer addition equations with `math:Math` blocks so that the code calculates the sum of 5 or more numbers. If the equation gets too long, then display using `game:show long text`

In order to combine multiple items we will need to add additional `math:Math` blocks

The splash screen is primarily designed for short sentences. This limits the length of equation we can effectively display. `game:show long text` allows for a better representation for longer text.

## Concept: Basic math operators with variables

We can convert variable based math equations, like A = B + C, into code using our code variables and math operators.

### Operators

In Python, the following order of operation precedence applies:

1. Multiplication (*) and Division (/)
2. Addition (+) and Subtraction (-)

Note: Python uses the* symbol for multiplication the / for division. In order to change order of these operations, you can use parentheses ( ) around expressions just like in math.

### Example #2: Displaying expressions with `game:splash` #example-2

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
2. Add a `variables:thirdNumber` variable with a unique value
3. Create an equation using both the addition operator (+) and the multiplication operator (*)
4. Swap the Addition and Multiplication operator and run the program (Typically the answers will differ)

### Student Task #3: Multiple operators and variables equation

1. Start with the code from the previous task
2. Add a `variables:fourthNumber` variable
3. Create an equation using 3 different operators
4. Challenge: create an equation using all 4 basic operators (+, -, *, /) and at least 5 unique variables

~hint
Look at the Python code. For multiple operator equations it is often easier to code in Python. Note how using parenthesis ( ) changes the equation.


### Student Task #4: Movement


### Student Task #5: Conversion

1. Create 2 variables
   1. `variables:tempC` (temperature Celsius)
   2. `variables:tempF` (temperature Fahrenheit)
2. Initialize `variables:tempC` with common Celsius temperature (for example, 22.0)
3. Create an equation using the formula:
   1. `variables:tempF` = `variables:tempC` × 9/5 + 32 and assign it to a new variable `variables:temp`
4. Show the `variables:temp` in a Splash Screen
5. Challenge: create an equation for converting back to Celsius:
    1. `variables:tempC` = (`variables:tempF` - 32) × 5/9
    2. pay careful attention to the parentheses

~hint
It can be difficult to structure complicated expressions using blocks. Look at and edit the Python code to create the formula where it looks much more like a standard math equation.

### Student Task #5: Debugging

We decided that we want to have three different variables in our code - `variables:a`, `variables:b`, and `variables:c`. The variable `variables:a` should be set to 3, `variables:b` should be set to a + 5, and `variables:c` should be set to a + 2 * b. This should result in `variables:a` storing 3, `variables:b` storing 8, and `variables:c` storing 19 at the end. When we wrote this out, though, we found that we couldn't run our code. What is going wrong in the following code, and how can you fix it?

Fix the Code here

image of code blocks with error

~hint
Click edit to fix code. `game:splash` can display string characters. Review the previous examples that use `game:splash`.

~
After you are able to run the code, the value of `variables:c` should be shown on the screen. There's a problem because the value shown is not quite right. Rearrange the existing blocks so that it produces the correct output, without removing or adding any JavaScript or blocks beyond what was necessary for part 1. What went wrong? Fix the output.

## Variables Summary

Variables are names that point to a container that can be updated to hold different data types.
Data Types used in variables so far are `variables:Sprite`, `variables:numbers` and `variables:strings`.

**Strings** are sequences of characters (like the letters found on a keyboard) surrounded by quotation marks.

Displaying a number often requires type coercion by using `text:join` to convert a number into a string.

## What We Learned

1. In Python what is the resulting value of answer for answer = 5 + 3 *2? Explain why the answer is not 16.
2. How is putting operators and numbers into a calculator different than writing in code (example: 2 + 3 + 4* 4)? Explain.
3. Research and describe 2 other `math:Math` operators found in the math menu in @boardname@ (hover over values for more information).

## Additional Resources

(Python Scope of Variables (article) - DataCamp)[https://www.datacamp.com/community/tutorials/scope-of-variables-python]
