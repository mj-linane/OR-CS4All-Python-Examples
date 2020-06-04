# CLASSES - PRIVATE ATTRIBUTES AND METHODS
class Dog(object):
    def __init__(self, name, birth_year):
        print("Hello I am new here")
        self.__name = name
        # PRIVATE ATTRIBUTE
        self.__birth_year = birth_year
        print("I was born in", self.__birth_year)

    # PRIVATE METHOD / FUNCTION
    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method")
        self.__private_method()

    # CONTROL ACCESS -- READ ACCESS

    @property
    def name(self):
        return self.__name

    # CONTROL ACCESS -- WRITE ACCESS

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name empty, please enter a new name")
        else:
            self.__name = new_name
            print(
                "Name change successful, new name is " +
                self.__name
            )

    @property
    def name(self):
        return self.__name

    # CONTROL ACCESS -- WRITE ACCESS

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name empty, please enter a new name")
        else:
            self.__name = new_name
            print("Name change successful, new name is " + self.__name)

    @property
    def name(self):
        return self.__name

    # CONTROL ACCESS -- WRITE ACCESS

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name empty, please enter a new name")
        else:
            self.__name = new_name
            print("Name change successful, new name is " + self.__name)


dog1 = Dog("Fred", 2010)

print(dog1.name)

# CHANGED NAME
# dog1.name = "Lassey"
dog1.name = ""
