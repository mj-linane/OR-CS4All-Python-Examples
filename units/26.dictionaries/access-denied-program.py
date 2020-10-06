# OVERVIEW
# An electronic door lock company wants you to design software to handle the door keypads.
# They are developing a keypad with a touch screen that would require 2 different inputs: The user's initials and their 4 digit passcode.

# SET UP DICTIONARY OF USERS
# Create a dictionary of sample data: pairs of initial keys and 4-digit codes as values to check the program
users = {}

# WELCOME USERS


def welcome_users():
    return
    # Print "Welcome To The [Make Up A Name] Security Company Console"
    # Then say "Where Security Is Our Middle Name"

# ASK FOR INITIALS AND PASSCODE


def ask_credentials():
    return
    # The user would input their initials and their 4-digit passcode.
    # They are then passed into the check_credentials function to see if they are cleared for entry
    check_credentials()

# CHECK USER DICTIONARY


def check_credentials(initials, passcode):
    return
    # If the initials exist in the dictionary and the passcode is the correct key, grant access and print to the screen "Access Granted"
    # Tell the user "Incorrect Passcode" if they put in the wrong passcode.
    # Tell the user "User Not Found" if their initials are not found in the dictionary.
    # Lastly, tell them to Press the enter key to exit.
