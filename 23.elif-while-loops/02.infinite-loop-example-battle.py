# Losing battle
# Warning about infinite looops

print("Your hero is surrounded by the enemy")
print("You are without backup")
print("Your hero draws their sword")

health = 100
trolls = 0
damage = 7

while health > 0:
    print("Your hero has ", health, "health")
    #trolls=trolls +1
    trolls += 1
    health -= damage

    print("Your hero swings and defeats a troll, but takes",
          damage, "damage points.")

print("Your hero fought bravely and defeated", trolls, "trolls.")
print("But your hero died in battle")
