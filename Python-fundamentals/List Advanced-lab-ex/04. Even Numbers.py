numbers_as_string = input().split(", ")
numbers_as_int = list(map(lambda x: int(x), numbers_as_string))
evens = list(map(lambda x: numbers_as_int.index(x), filter(lambda x: x % 2 == 0, numbers_as_int)))
print(evens)







