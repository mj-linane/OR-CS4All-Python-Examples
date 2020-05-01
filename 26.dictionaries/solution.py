# DICTIONARIES

# CREATING A NEW DICTIONARY
# KEY - VALUE PAIRS
person1 = {
    'Name': 'MJ',
    'Job': 'Teacher',
    'Age': 24,
    'Location': 'Massachusetts',
    'Hobbies': ['coding', 'video games'],
    'Bio': {'height': 6, 'weight': 175},

}

# GET DICTIONARY VALUE (USING KEY)
x = person1['Name']

# GET ALL KEYS
x = person1.keys()

# for key in person1.keys():
# print(key)

# GET LENGTH OF DICTIONARY
x = len(person1)

# ADD NEW KEY-VALUE TO A DICTIONARY
person1.update({'Favorite Coding Language': 'Python'})

# UPDATE A VALUE
person1['Age'] = 25

# DELETE A KEY-VALUE
del person1['Age']

# GET ALL VALUES

x = person1.values()

# for value in person1.values():
#   print(value)

# GETTING VALUE IN LIST INSIDE OF DICTIONARY
x = person1['Hobbies'][0]

# GETTING VALUE IN DICTIONARY INSIDE OF DICTIONARY
x = person1['Bio']['height']

# COMPARE DICTIONARIES
boys = {
    'Jack': 18,
    'Charlie': 15,
    'Bob': 18,
}

girls = {
    'Julia': 16,
    'Mary': 15,
}

for boy in boys.keys():
    if boy in girls.keys():
        print(True)
    else:
        print(False)

# CHALLENGE #1
"""
Create dictionary of viruses and their rate of infection

R0 dictionary
Seasonal Flu - 1.3
SARS - 2-5, [2, 5]
HIV - 2-5
Measels - 12-16
Coronavirus/covid-19 - 2-3
Zombie Virus - R?

"""

# CHALLENGE #2
"""
Create 3 viruses in Python using dictionaries
Each will have a key value pair of:
-NAME
-INFECTION PROBABILITY
-LETHALITY PROBABILITY
"""
