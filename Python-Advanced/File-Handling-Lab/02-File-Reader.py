with open("numbers.txt", "r") as file:
    numbers = [int(el.rstrip()) for el in file.readlines()]
    print(sum(numbers))