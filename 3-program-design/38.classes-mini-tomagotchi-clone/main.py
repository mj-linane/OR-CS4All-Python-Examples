# Pet Caretaker
# A virtual pet to care for

from random import randrange


class Pet(object):
    """A virtual pet"""
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grr..."']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        self.excitement += 1
        self.food += 1

    def mood(self):
        if self.food > self.food_warning and \
                self.excitement > self.excitement_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "\nI'm " + self.name + "." + "\nI feel " + self.mood() + "."
        return state

    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        print(
            "I'm a" +
            self.animal_type +
            self.name +
            " and I feel" +
            self.mood +
            " now.\n"
        )
        print(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()

    def feed(self):
        print("**crunch**\n mmm.  Thank you.")
        meal = randrange(self.food, self.food_max)
        self.food += meal
        if self.food < 0:
            self.food = 0
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I'm full!")
        self.__clock_tick()

    def play(self):
        print("Woohoo!")
        fun = randrange(self.excitement, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("I'm excited!")
        self.__clock_tick()


def main():
    pet_name = input("What do you want to name your pet? ")
    pet_type = input("What type of animal is your pet? ")
    my_pet = Pet(pet_name, pet_type)

    input(
        "Hello! I am " +
        my_pet.name +
        " and I am new here. \n Press enter to start."
    )

    choice = None

    while choice != "0":
        print("""
        ***INTERACT WITH YOUR PET***

        1 - Feed your pet
        2 - Talk with your pet
        3 - Teach your pet a new word
        4 - Play with your pet
        0 - Quit
        """)

        choice = input("Choice: ")

        # exit
        if choice == "0":
            print("Good-bye.")

        # feed your pet
        elif choice == "1":
            my_pet.feed()

        # listen to your pet
        elif choice == "2":
            my_pet.talk()

        # teach your pet new word
        elif choice == "3":
            new_word = input("What is the new word?")
            my_pet.teach(new_word)

        # play with your pet
        elif choice == "4":
            my_pet.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
("\n\nPress the enter key to exit.")
