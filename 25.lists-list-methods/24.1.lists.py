# Python Lists
# Adventurer's Backpack

# Create A List
# backpack = ["sword", "helmet", "food", "healing potion", "coins"]

# Find Length List
# print(len(backpack))

# Test if Item Is In Backpack
# life = 20
# if "mana potion" in backpack:
#   print("I am healed!")
# else:
#   life -= 2
#   print(life)

# Indexing List

# -3    -2    -1
# ["a", "b", "c"]
#   0    1    2

# Find an Item At An Index Position
# print(backpack[-1])

# Find Multiple Items Using Slice
# |"a"| "b"| "c"|

# start = 1
# finish = 3
# print(backpack[start:finish])

# Remove an Item
# del backpack[0]
# print(backpack[0])

# # Remove Multiple Items
# del backpack[0:2]
# print(backpack)

# # Add A New Item

# backpack.append("bread")
# print(backpack)

# # Concatenate Lists
# additional = ["armor", "shoes"]
# backpack += additional
# print(backpack)

# # Redefine Items At Index Positions
# backpack[0] = "healing potions"
# print(backpack)

# LIST METHODS - SCORE TRACKER PROGRAM

scores = []
user_select = None

# Display Menu
while user_select != "0":
    print(
        """
    0 - Exit
    1 - Show All Scores
    2 - Add A New Score
    3 - Delete A Score
    4 - Sort All Scores
    """
    )

    user_select = input("Select an option:")

    # exit
    if user_select == "0":
        print("Good bye")

    # List High Scores
    elif user_select == "1":
        print("High Scores")
        for score in scores:
            print(score)

    # Add A Score
    elif user_select == "2":
        score = int(input("What score do you want to add?"))
        # ADD ITEM WITH APPEND
        scores.append(score)

    # Remove A Score
    elif user_select == "3":
        score = int(input("What score do you want to remove?"))
        if score in scores:
            # DELETE USING THE REMOVE METHOD
            score.remove(score)
        else:
            print("That score isn't on the list")

    # Sort All Scores
    elif user_select == "4":
        scores.sort(reverse=True)

    else:
        print("That is not an option")
