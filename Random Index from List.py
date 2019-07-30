# Python3 code to demonstrate
# to get random number from list
# using random.randrange

import random

n, m = input().split()
n = int(n)
m = int(m)

a = []

for i in range(0, m):
    x = int(input())
    y = int(input())
    a[x] = y
    pass

while m > 0:
    x = int(input())
    print(a[x])
    m -= 1
    pass

# using random.randrange() to
# get a random number from the entire list
random_number = random.randrange(len(a))
random_element = a[random_number]
