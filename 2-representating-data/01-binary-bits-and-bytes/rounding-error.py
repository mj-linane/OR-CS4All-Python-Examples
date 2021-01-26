from decimal import Decimal


def square_root(num):
    root = 0.0
    while root * root < num:
        root += 0.01
    return root


# Run Square Root Tests
print(square_root(4))
print(square_root(9))

# Shows the full decimal
print(Decimal(.01))
print(1.2-1.1)
print(Decimal(1.2) + Decimal(1.0))
