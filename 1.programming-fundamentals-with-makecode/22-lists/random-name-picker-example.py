import random


def pick_person():
    number_of_people = int(
        input("How many people do you want to randomly pick from?\n"))
    people = []
    for i in range(1, number_of_people + 1):
        print("What is the name of person %d?" % i)
        people.append(input())
    pick = random.randint(0, len(people))
    print("The chosen one is " + people[pick])

    print("Would you like to go again? [y/n]")
    reset = input().lower()
    if reset == "yes" or "y" or "yep":
        pick_person()


pick_person()
