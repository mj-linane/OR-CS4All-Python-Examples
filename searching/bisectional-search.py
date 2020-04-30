"""
Create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an
integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input -
is its guess too high or too low? Using bisection search,
the computer will guess the user's secret number!
"""


# User thinks of an interget between 0 and 100.
print('Please think of a number between 0 and 100!')

# RANGE OF NUMBERS
high = 100
low = 0
guess = 50

#MAIN LOOP
while True:
  print('Is your secret number '+str(guess)+'?')
  clue = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  # Checks response
  if clue == 'c':
    break
  elif clue == 'h':
    high=guess
    guess = int((high+low)/2)
  elif clue == 'l':
    low=guess
    guess = int((high+low)/2)
  else:
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number is', guess)

# ORIGINAL CODE/ALGORITHM
# Works going up all the way and down all the way but when the second guess is not low, low, low, but low, high, low, it breaks.


# max_num = 0
# min_num = 50
# is_right = False

# while is_right == False:
#     print('Is your secret number ', newguess, '?')
#     clue = input(
#         "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#     if clue == 'c':
#         is_right == True
#         print('Game over. Your secret number is', newguess)
#     elif clue == 'h':
#         lastguess = newguess
#         newguess = int(lastguess/2)
#         print(newguess)
#     else:
#         lastguess = newguess
#         newguess = int(lastguess+((100-lastguess)/2))
#         print(newguess)