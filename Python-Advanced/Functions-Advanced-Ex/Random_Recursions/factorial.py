def first_way_factorial(x):
    if x == 1:
        return 1
    else:
        return x * first_way_factorial(x - 1)


def second_way_factorial(x):
    factorial = 1
    for el in range(1, x + 1):
        factorial *= el
    return factorial


def third_way_factorial(x, y=1):
    if x == 1:
        return y
    else:
        return third_way_factorial(x - 1, y * x)

print(third_way_factorial(4))
print(second_way_factorial(4))
print(first_way_factorial(4))