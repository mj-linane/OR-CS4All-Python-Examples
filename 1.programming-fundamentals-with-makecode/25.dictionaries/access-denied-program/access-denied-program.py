# SET UP DICTIONARY OF USERS
# Create a dictionary of sample data: pairs of initial keys and 4-digit codes as values to check the program.

# TODO: Add 4 users to the dictionary and give each a different passcode.
users = {}  # Example: 'ML': '1234'


# WELCOME USERS
def welcome_users():
    pass
    # TODO: Change the name in the print statement below to be your name
    print("Welcome To The [Make Up A Name] Security Company")
    print("Where Security Is Our Middle Name")


# CHECK USER DICTIONARY
def check_credentials():
    # Ask the user for their initials
    name = input("Enter Your User Initials: ")

    # Ask the user to input their 4-digit passcode
    passcode = input("Enter Your Pass Code? ")

    # FINISH THE PROGRAM

    '''TODOS 
    1. Write an if statement that checks to see if the user is in the dictionary 
    2.      If the user in the dictionary, write another if statement that checks to see if the passcode they entered is 
            correct. If that password for that user is correct, 
                add a print statement that says "Access Granted"
    4.      Add an else statement that prints "Incorrect Password. Access Denied"
    5. Add an else to the first if statement that says "User Not Found"
    '''


# RUN MAIN PROGRAM
def main():
    welcome_users()
    check_credentials()


if __name__ == "__main__":
    main()
