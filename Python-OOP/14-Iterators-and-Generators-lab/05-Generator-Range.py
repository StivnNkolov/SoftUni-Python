def genrange(start, end):
    while start <= end:
        yield start
        start += 1


number = (el for el in range(1, 11))
print(list(number))
print(type(number))

numbers = genrange(1, 10)
print(list(numbers))
print(type(numbers))
