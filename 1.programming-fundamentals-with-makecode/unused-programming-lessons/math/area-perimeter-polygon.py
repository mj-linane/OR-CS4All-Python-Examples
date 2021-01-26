import math

# A regular polygon has n number of sides. Each side has length s.
# Takes 2 arguments, n and s. This function should sum the area and
# square of the perimeter of the regular polygon. The function returns the sum,
# rounded to 4 decimal places.

pi = round(math.pi, 5)


def polysum(n, s):
    area = (0.25*n*s ^ 2)/pi(pi/n)
    perimeter = s ^ s
    return round(area+perimeter, 4)


print(polysum(4, 10))
