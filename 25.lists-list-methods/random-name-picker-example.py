import random


def pick_person():
    NumberOfPeople = int(
        input("How many people do you want to randomly pick from?\n"))
    peopleslist = []
    for i in range(1, NumberOfPeople + 1):
        print("What is the name of person %d?" % i)
        peopleslist.append(input())
    pick = random.randint(0, len(peopleslist))
    print("The chosen one is " + peopleslist[pick])

    print("Would you like to go again? [y/n]")
    reset = input().lower()
    if reset == "yes" or "y" or "yep":
        pick_person()


pick_person()
