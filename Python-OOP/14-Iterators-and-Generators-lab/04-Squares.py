def squares(end_value):
    work_value = 1

    while work_value <= end_value:
        yield work_value ** 2
        work_value += 1


for el in squares(5):
    print(el)
