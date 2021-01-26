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


def add_short(x, y):
    return x + y


print(add_short(2, 3))


def add_multi(x, y):
    return (
            x +
            y
    )


print(add_multi(2, 3))
