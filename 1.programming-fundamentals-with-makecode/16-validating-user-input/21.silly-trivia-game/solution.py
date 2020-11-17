"""
INSTRUCTIONS
A theme park wants to create a program that will run on monitors as visitors are standing in line for a fun house ride. They want us to get some user data and then print back a bunch of silly trivia information about them. 

Because we are just building a prototype, we can just send every answer to the console. So, here are their requests:
"""

# Part 1: greeting section
"""
Greet the user
Ask for their name
Ask for age.
Ask for their weight.
"""
print("Hello!")
name = input("What is your name?")
age = input("How old are you?")
weight = input("How much do you weigh?")

# Part 2: An Email from a Poet
"""
Print their name in all lower case and "If poet e. e. cummings were to email you, he'd address you as (lower case name)"
"""
print("If poet ee cummings were to email you, he'd address you as " + name.lower())

# Alternative way of printing
# print("If poet ee cummings were to email you, he'd address you as ", name.lower())

print("But if ee were mad, he'd call you " + name.upper())

# Part 3: Annoying Child
"""
Have the screen say, "if a child were to try and get your attention, they might do it as" and print their name 5 times.
"""
repeat_Name = (name + " ") * 5
print("If a small child were to try and get your attention, they might do it as " + repeat_Name)

# Part 4: Age In Seconds
"""
Print to the screen the user's age in seconds.
"""
seconds = int(age) * 60 * 60 * 24 * 365
print("You're over " + str(seconds) + " seconds old.")

# Part 5: Weight Calculation
"""
Calculate their weight on the moon.
Calculate their weight on the sun.
"""
moon_weight = int(weight) / 6
print("Did you know that on the moon you would weigh only " +
      str(moon_weight) + " pounds")

sun_weight = int(weight) * 27.1
print("On the sun, you'd weigh " + str(sun_weight) + " pounds...but not for long")

# Part 6: User press enter
"""
Wait for the user to exit by pressing "enter". The screen should say "Press the enter key to exit".
"""

input("Press the enter key to exit.")
