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
print(person1['Name'])

# GET ALL KEYS
print(person1.keys())

for key in person1.keys():
    print(key)


# GET LENGTH OF DICTIONARY
print("The length of person1 is: " + str(len(person1)))

# ADD NEW KEY-VALUE TO A DICTIONARY
person1.update({'Favorite Coding Language': 'Python'})

# UPDATE A VALUE
person1['Age'] = 25

# DELETE A KEY-VALUE
del person1['Age']
print(person1)

# GET ALL VALUES
print(person1.values())

for value in person1.values():
    print(value)

# GETTING VALUE IN LIST INSIDE OF DICTIONARY
print(person1['Hobbies'][0])

# GETTING VALUE IN DICTIONARY INSIDE OF DICTIONARY
print(person1['Bio']['height'])

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

# PRACTICE CHALLENGES
"""
# CHALLENGE #1

1. Create dictionary called `viruses`. 
2. Put the name of the virus as the value
3. Put the rate of infection as the key for each virus. 
Virus infection rates are measure at how many people can a single person infect, represented by "R0"

Seasonal Flu - 1.3
SARS - 3.5 # true range is 2-5 
HIV - 3.5 # true range is 2-5
Measles - 14 # true range is 12-16
Coronavirus/covid-19 - 2.5 #true range is 2-3
Zombie Virus - R?

"""

"""
# CHALLENGE #2

Create 3 viruses in Python using dictionaries
Each will have a key value pair of:
-NAME
-INFECTION PROBABILITY
"""
