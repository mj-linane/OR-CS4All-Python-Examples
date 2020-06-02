# OBJECT ORIENTED PROGRAMMING AND CLASSES -- Using Object Attributes

"""
# Part 1: INITIALIZING AN OBJECT ATTRIBUTE
"""


class Dog(object):

    def __init__(self, name):
        print("Hello! I am new here.")
        # Initialize attribute on copy creation
        self.name = name

    """
    PART 2: ACCESSING OBJECT ATTRIBUTES
    Attributes can be used throughout the object as a stand-in variable
    for the input later on.
    """

    def say_hello(self):
        print("Woof!!!" + "\n" + "My name is: " + self.name)


# MAIN PROGRAM
beagle = Dog("Fred")
beagle.say_hello()

"""
PART 3: PRINTING AN OBJECT
Let's try printing out the dog/object
"""

# print(beagle)

"""
We see that it tells us: <__main__.Dog object at 0x00E46148>
That means that it is a Dog object and
it gives us the memory location that it is stored.

Ok, that at least tells us what it is. But there has to be more to it.

We can use the __str__() method in a class definition.
That give us the ability to control what gets printed out about a
class object.
"""


# class Dog(object):

#     def __init__(self, name):
#         print("Hello! I am new here.")
#         # Initialize attribute on copy creation
#         self.name = name

#     """
#     PART 3: ADD STR
#     """
#     # PRINT STRING

#     def __str__(self):
#         header1 = "Dog object\n"
#         header2 = "name: " + self.name

#         return (
#             header1 +
#             header2
#         )

#     def say_hello(self):
#         print("Woof!!!" + "\n" + "My name is: " + self.name)


# MAIN PROGRAM
# beagle = Dog("Fred")

"""
And now, when we print out the dog,
Python should tell us a little bit
more about it
"""
# print(beagle)


"""
PART 4: ADDING CLASS ATTRIBUTES
Problem: Track the number of dogs that have been created.
Possible solution? Create a global variable? Change it
every time that an object is instantiated?

No...

Easier solution -- Class Attributes
Python already tracks this for us in what is called a
Class Attribute. An attribute that is on the parent class
and stays on the parent class.

This can be accessed using class attribute.

"""

# class Dog(object):
#     """
#     PART 4: ADD A CLASS ATTRIBUTE

#     We create the num_dogs variable to track the number of dogs
#     """
#     num_dogs = 0

#     def __init__(self, name):
#         print("Hello! I am new here.")
#         self.name = name
#         """
#         We all so iterate the variable.
#         Every time a new dog is created, it increases the class total by 1
#         """
#         Dog.num_dogs += 1

#     def __str__(self):
#         header1 = "Dog object\n"
#         header2 = "name: " + self.name

#         return (
#             header1 +
#             header2
#         )

#     def say_hello(self):
#         print("Woof!!!" + "\n" + "My name is: " + self.name)


# """
# ACCESSING CLASS ATTRIBUTE

# We can access by going to class itself and access that attribute:
# """

# print(
#     "The current total number of dogs through num_dogs attribute is:",
#     Dog.num_dogs
# )

"""
PART 5: ACCESSING CLASS ATTRIBUTE WITH STATIC METHOD

The second way we can access that number is by going
to the child objects and calling
the static method that reports the number of dogs for us.
"""


class Dog(object):
    """Dog base class.

    Arguments:
        name {string} -- name of the dog.

    Returns:
        object -- returns a new Dog object.
    """
    num_dogs = 0

    """
    PART 5: ADD STATIC METHOD
    """
    @staticmethod
    def count():
        print("The total number of dogs created is:", Dog.num_dogs)

    """
    Notice: the static method doesn't have self...that is because
    it is attached to the Dog class, not to the dog objects
    that are instantiated/copied

    Also, what is with the @ symbol? That is called a decorator...
    It modifies a function/method and you put it right before
    the function is defined.

    """

    def __init__(self, name):
        print("Hello! I am new here.")
        self.name = name
        Dog.num_dogs += 1

    def __str__(self):
        """details object when printed

        Returns:
            string -- object type and name
        """
        header1 = "Dog object\n"
        header2 = "name: " + self.name

        return (
            header1 +
            header2
        )

    def say_hello(self):
        print("Woof!!!" + "\n" + "My name is: " + self.name)


# CREATING DOGS
print("Creating more dogs...")
dog1 = Dog("Fred")
dog2 = Dog("Alice")
dog3 = Dog("Daisy")

dog1.count()

dog4 = Dog("Bill")

Dog
