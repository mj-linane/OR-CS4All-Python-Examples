---
title: 'Validating User Input'
author: 'MJ Linane'
date: '10-20-2020'
course: 'G:\My Drive\.work-code\or-cs4all-python-lesson-plans\1.intro-sprite-game'
lesson number: ''
---

## Activity: User Input and String Logic

Logical expressions like `if` and `else` condition checks can be to used for much more than comparing numeric values. Data type values (such as Strings) can be compared and used to change the way the programs we write behave depending on the different conditions.

Some of the earliest computer games, text-based adventure games, used only text based responses to have the player interact with the story. The game prompts the user with a question, accepts the user's answer,  and calculates what response should be provided.

In this activity, you will use:

* `game.ask()`
* `game.ask_for_string("What is your name?")`
* Use Boolean logic with Strings

## Concept: User interaction

Allowing users to interact with your code is an important step in making an interesting and enjoyable game. Logical expressions play an important part in making your code react to that user input, even with something as simple as a "yes or no" question.

[![Link to Video](/static/thumbnail_play_video.png)](https://aka.ms/40546a-logic-input)

### Example #1: asking_a_question

1. Review the code below
2. Identify what condition makes you win (and what that means about what `game.ask()` turns into)

```python
  if game.ask("Do you want to win?") == True:
    game.splash("You win!")
```

In this simple game, the only options are to press `A` to win, or `B` to do nothing. This illustrates two important concepts:

>* **Built in** methods can return boolean values, allowing us to easily create logical tests in our code.
>* Tests can be based off user input - in this case, which button the user pressed.

### Project Task #1: option_for_failure

1. Create new project called `option_for_failure`.
2. Start with the code from example above.
3. Add an `else` branch to the `if` statement - use `game.splash()` to say "Bye"
4. Add an `elif` statement which provides an "option for failure." Use a `game.ask()` that asks "Do you want to lose?"
5. Make sure the player only gets the "You lost!" message if they respond "OK" to the prompt from step 3

## Concept: Text input

Beyond asking questions with a binary response (for example, "yes or no" or "true or false"), we can request input from users and keep track of that information to enhance the player's experience. We could ask for a user name and display the name in later in the game, such as in a leader board or a welcome message as in example #2.

### Example #2: Taking in a user name

1. Review the code below
2. Create the sample code and run the code
3. Identify how the users input affects the game

```python
user_name = game.ask("What is your name?")
game.splash("Hello " + user_name + "!")
```

Prompts for names, like above, allows games to be more personal. The prompts can also enable users to make choices during game play, or make guesses from clues to solve a puzzle, or to use a password.

### Project Task #2: making_a_secret_password

1. Create a new project called `making_a_secret_password`
2. Start with the code from example #2.
3. Create a new variable (`user_password`)
4. Set `user_password` to get the result of `game.ask_for_string()`. Inside of the parenthesis of `game.ask()`, type "What is your password?". Any text inside of the parenthesis is called the "parameter" and will be passed into the function.
5. Create an `if-else` statement
6. For the `if` condition, check to see if `user_password=="Arcade"`. This checks the input to see if it equals the string, "Arcade".
7. If those two are the same, `game.splash()` the phrase "login successful"
8. Otherwise, `game.splash()` the phrase "login failed"

#### Optional Challenge

Use the `or` operator to also compare your stored password with "\*\*\*\*\*\*\*" and accept the password if the user's input is equal to **either** "\*\*\*\*\*\*\*" **or** "Arcade".
