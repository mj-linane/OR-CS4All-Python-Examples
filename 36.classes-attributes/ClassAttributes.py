# OBJECT ORIENTED PROGRAMMING AND CLASSES

# DOG
# Characteristics: gender, breed, age, hair color, weight, temperament
# Actions: Run, sit, eat

"""
OOP sounds complicated but actually really simple

Take a real world object and consider how could we code that in real life?


"""
# CODING A DOG'S BEHAVIORS (METHODS) WITH FUNCTIONS


def bark():
    print("Bark!")


# CODING A DOG'S ATTRIBUTES
# OPTION 1: VARIABLES
gender = 'male'
breed = 'great dane'
age = 13

# OPTION 2: DICTIONARY
dog = {
    'name': 'Ghost',
    'gender': 'male',
    'breed': 'great dane',
    'age': 13,
}


# OPTION 3: CLASS
"""
What is a class?
A template/blueprint that can be copied
with all of the existing attributes and methods

Can create many objects from the same class.

Each object/instance coming from the same class,
will have a similar structure.

For instance, every dog is going to be able to
similar things, with some differing attributes and behaviors.
"""

# PART 1: BUILDING A CLASS


# Define a class


# class Dog(object):
#     """A Virtual Dog"""

#     # Define a method
#     def say_hello(self):
#         print("Hello! I am an instance of a dog. I am new here")

#     def bark(self):
#         print("Woof!!!")


"""
What is "self"?
Methods are functions associated with an object. It has one parameter: self.
It doesn't actually use self. The parameter provides a way for a
method to refer to the object itself.
"""

# bulldog = Dog()

# PART 2: BUILDING A CONSTRUCTOR
"""A Virtual Dog"""


class Dog(object):
    """
    Constructor, special function used by Python,
    runs as soon as a copy is made
    Anything with two __ at the beginning is a
    "special method" by python itself

    __init__ is automatically called.
    """

    def __init__(self):
        print("Hello! I am new here.")

    def say_hello(self):
        print("Hello! I am an instance of a dog. I am new here")

    def bark(self):
        print("Woof!!!")


# PART 3: CREATING MULTIPLE OBJECTS
beagle = Dog()
poodle = Dog("Ghost", 2)
