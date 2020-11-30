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
    person1['Age'] = 30
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

