command = input()

phone_book = {}

while not command.isdigit():
    name, number = tuple(command.split("-"))
    phone_book[name] = number

    command = input()

searches = int(command)

for _ in range(searches):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
