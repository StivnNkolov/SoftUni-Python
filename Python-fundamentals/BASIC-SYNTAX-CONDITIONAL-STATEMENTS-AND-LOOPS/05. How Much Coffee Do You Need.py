coffee_taken = 0

command = input()

while not command == "END":
    if command.lower() == "coding":
        if command.isupper():
            coffee_taken += 2
        else:
            coffee_taken += 1
    elif command.lower() == "dog" or command.lower() == "cat":
        if command.isupper():
            coffee_taken += 2
        else:
            coffee_taken += 1
    elif command.lower() == "movie":
        if command.isupper():
            coffee_taken += 2
        else:
            coffee_taken += 1
    command = input()

    if command == "END":
        if coffee_taken > 5:
            print("You need extra sleep")
        else:
            print(coffee_taken)
