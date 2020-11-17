# Adventurer's Backpack

# Create A List
backpack = ["sword", "helmet", "food", "healing potion", "coins"]

# Find Length List
print(len(backpack))

# Test if Item Is In Backpack
life = 20
if "mana potion" in backpack:
    print("I am healed!")
else:
    life -= 2
    print(life)

# Indexing List

# -3    -2    -1
["a", "b", "c"]
# 0    1    2

# Find an Item At An Index Position
print(backpack[-1])

# Find Multiple Items Using Slice
# |"a"| "b"| "c"|

start = 1
finish = 3
print(backpack[start:finish])

# Remove an Item
del backpack[0]

# Remove Multiple Items
del backpack[0:2]

# Add A New Item

backpack.append("bread")

# Concatenate Lists
additional = ["armor", "shoes"]
backpack += additional

# Redefine Items At Index Positions
backpack[0] = "healing potions"

print(backpack)
