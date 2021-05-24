def searching_for_contact(input_command, data):
    input_command = int(input_command)
    for _ in range(input_command):
        searched_name = input()
        if searched_name in data:
            print(f"{searched_name} -> {data[searched_name]}")
        else:
            print(f"Contact {searched_name} does not exist.")


def creating_our_phonebook(input_command):
    phone_book = {}
    while not input_command.isdigit():
        name, number = tuple(input_command.split("-"))
        phone_book[name] = number
        input_command = input()

    command = int(input_command)

    searching_for_contact(command, phone_book)

    return phone_book


contacts = creating_our_phonebook(input())
