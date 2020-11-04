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
