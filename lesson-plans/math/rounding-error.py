# Why doesn't Python print out 1.0?
# to learn more https://docs.python.org/3/tutorial/floatingpoint.html


"""
In Python, there are 53 bits of precision available for floating point numbers
so the digits stored for the decimal number 0.1 will be
11001100110011001100110011001100110011001100110011001
This is equivalent to the decimal number
0.1000000000000000055511151231257827021181583404541015625
close to 1/10th but not 1/10th. Just remember, even though 
the printed result looks like the exact value of 1/10, 
the actual stored value is the nearest representable binary fraction.
"""

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')
