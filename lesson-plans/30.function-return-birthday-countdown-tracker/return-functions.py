# def add(x,y):
#   answer = x+y
#   print(answer)

# add(1,2)


def add(x, y):
    answer = x + y
    return answer


add_answer = add(1, 2)
print(add_answer)

# Shortened form


def addShort(x, y):
    return x + y


print(addShort(2, 3))


def addMulti(x, y):
    return (
        x +
        y
    )


print(addMulti(2, 3))
