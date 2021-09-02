def multiplier(outter_value):
    def inner(inner_value):
        return outter_value * inner_value

    return inner


multiply_10 = multiplier(10)
output = multiply_10(8), multiply_10(7.7)


def compare_(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


compare = lambda a, b: 1 if a > b else (-1 if a < b else 0)


def sum_(a, b):
    return a + b


sum = lambda a, b: a + b
