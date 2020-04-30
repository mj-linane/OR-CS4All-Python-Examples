# RULES
# Dictionaries are key:value pairs

# More than one entry per key is not allowed ( no duplicate key is allowed)

# The values in the dictionary can be of any type while the keys must be immutable like numbers, tuples or strings.

# Dictionary keys are case sensitive- Same key name but with the different case are treated as different keys in Python dictionaries.

# CREATE A DICTIONARY OBJECT
person1 = {
    'Name': 'MJ',
    'Job': 'Teacher',
    'Age': 34,
    'Location': 'Mattapoisett',
    'Number of Students': None,
}

# PRINT A DICTIONARY VALUE BY GIVING KEY
x = person1['Name']

# GET LENGTH OF A DICTIONARY
x = len(person1)

# UPDATING A DICTIONARY
person1.update({'Favorite Language': 'Python'})

# or we can do it using variables
person1['Number of Students'] = 100

x = person1

# DELETE KEYS FROM DICTIONARY
del person1['Age']
x = person1

# GET A LIST OF ITEMS IN THE DICTIONARY
students = {'Jack': 18, 'Charlie': 15, 'Amber': 16, 'Robert': 18}

x = students.items()

# DO SOMETHING TO EACH KEY
for key in students.keys():
    print(key)

# CHECK ALL VALUES
students.values()

# CHECK TO SEE IF A VALUE ALREADY EXISTS IN A DICTIONARY

# Here we have two sub-dictionaries "Boys" and "Girls", now we want to check whether our dictionary Boys exist in our main "students" dictionary or not.

boys = {'Jack': 18, 'Charlie': 15, 'Robert': 18}
girls = {'Amber': 16}
for key in list(students.keys()):
    if key in list(boys.keys()):
        print(True)
    else:
        print(False)

print(students.items())
print(x)

# DO THIS:
# Create 3 viruses in Python using dictionaries
# Each will have a key value pair of:
# -NAME
# -INFECTION PROBABILITY
# -LETHALITY PROBABILITY
