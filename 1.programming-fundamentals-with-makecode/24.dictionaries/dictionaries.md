---
title: 'Dictionaries'
---

## Overview
All of the compound data types we have studied in detail so far — strings and lists are sequence types, which use
 integers as indices to access the values they contain within them. Example is `list[0]`.
 
 Dictionaries are different. They use Python's built in mapping feature to map `keys` to `values`.
 
 ## Dictionary Syntax

### CREATING A NEW DICTIONARY
To create an empty dictionary:

```python
my_dictionary = {}
```

To create a dictionary with items inside of it:

```python
my_dictionary = {'one': 'uno'}
settings = {'single_player' : True}
characters = {
    'player1': 'Mario',
    'player2': 'Luigi'
}
```

### KEY - VALUE PAIRS

```python
person1 = {
    'Name': 'MJ',
    'Job': 'Teacher',
    'Age': 24,
    'Location': 'Massachusetts',
    'Hobbies': ['coding', 'video games'],
    'Bio': {'height': 6, 'weight': 175},

}
```
### GET DICTIONARY VALUE (USING KEY)

```python
person1['Name']
```
### CHECK TO SEE IF VALUE IN DICTIONARY

```python
try:
    person1['Age"] = 30
except KeyError:
    pass
```
    
or

```python
if "hobbies" in person1:
    person1['blah'] = 'coding' 
```

### GET ALL KEYS

```python
person1.keys()

for key in person1.keys():
    print(key)
```

### GET LENGTH OF DICTIONARY

```python
len(person1)
```
### ADD NEW KEY-VALUE TO A DICTIONARY

```python
person1.update({'Favorite Coding Language': 'Python'})
```

### UPDATE A VALUE

```python
person1['Age'] = 25
```

### DELETE A KEY-VALUE

```python
del person1['Age']
```

### GET ALL VALUES

```python
person1.values()

for value in person1.values():
    print(value)
```

### GETTING VALUE IN LIST INSIDE OF DICTIONARY

```python
person1['Hobbies'][0]
```

### GETTING VALUE IN DICTIONARY INSIDE OF DICTIONARY

```python
person1['Bio']['height']
```

### COMPARE DICTIONARIES

```python
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
```

## Practice #2 - dict-virus

* Create 3 new variables that will be the name of viruses.
* Assign a dictionary for each variable. 
* For each virus/dictionary, add a key value pair for INFECTION PROBABILITY (see below)

Virus infection rates are measure at how many people can a single person infect, represented by "R0"

* Seasonal Flu - 1.3
* SARS - 3.5 # true range is 2-5 
* HIV - 3.5 # true range is 2-5
* Measles - 14 # true range is 12-16
* Coronavirus/covid-19 - 2.5 #true range is 2-3
* Zombie Virus - R?

## Practice #2 - dict-r0

1. Create dictionary called `viruses`. 
2. Put the name of the virus as the value
3. Put the rate of infection as the key for each virus. 


## Project #1 Interview with a Turkey
1. Create a sprite called `my_turkey`
2. Create a dictionary called `turkey_info`
3. Put in at least 5 key-value pairs into the dictionary that tells us about that turkey. For instance, `age` or `name`.
4. Create a dialogue sequence whereby:
    1. Turkey greets user
    2. Turkey asks the user what they want to know about him/her
    3. Turkey lists off each of the keys in a long text box.
    4. Turkey asks `what do you want to know about me?`
    4. Game accepts user input and compares it in if-elif-else statement.
        1. `if` the user input matches the key in the turkey dictionary, then print out the value. An
         example print out might be: `my name is my_turkey['name']`.
        2. Add `elif` statements that print the remaining statements for the remaining keys.
        2. Add an `else` in which the turkey says something like `sorry I am not sure what you mean`

### Optional Challenges

1. Add more than 5 key-value pairs.
2. Set the whole interview into a `while` loop to give the user another chance at asking a question.
