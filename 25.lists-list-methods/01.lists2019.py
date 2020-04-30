import random
# CREATING A LIST
mixedlist = ['names', 10, ['another list', 'of stuff']]

favorites = ["pie", "dogs", "computers"]

notfavorites = ["cats", "teaching history"]

# PRINT A LIST
x = favorites

# GET LENGTH OF THE LIST
x = len(favorites)

# REMOVE ITEM OFF OF THE LIST AT INDEX POSITION
x = favorites[2]

# REMOVE RANDOM ITEM FROM THE LIST -- KNOW LIST LENGTH
x = favorites[random.randint(0, 2)]

# REMOVE RANDOM ITEM FROM THE LIST -- DON'T KNOW LIST LENGTH
'''
get length of the list and -1 because the index position will always be 1 less than the total number of items in the list
'''
x = favorites[random.randint(0, len(favorites)-1)]
print(x)

# ADD ITEMS TO THE END OF THE LIST
favorites.append("mj linane")
x = favorites

# REMOVING ITEMS FROM THE LIST AT INDEX POSITION
del favorites[0]

x = favorites

# REMOVING LAST ITEM FROM THE LIST
favorites.pop()

# COMBINING LISTS
x = favorites = ["pie", "dogs", "computers"] + ["cats", "teaching history"]

# or using the + operator on the variables
x = favorites + notfavorites

# CHECK FOR COMMON ITEMS IN 2 LISTS
x = any(item in favorites for item in notfavorites)
if x == True:
    print("True")
else:
    print("False")

# CHECK TO SEE IF ITEM IS IN THE LIST
if 3 in favorites:
    print('its there!')

# TO PERFORM AN ACTION ON EACH ITEM IN THE LIST
# for item in favorites:
#     print(item)

# SORT A LIST
print(favorites.sort())

# Guest List App
# guestlist = []
# while len(guestlist)<5:
#   username = input('Enter Guest Name')
#   print('REGISTERED')
#   guestlist.append('username')
# print('SOLD OUT')
