def adding_new_names_from_input(number):
    unique_names = set()

    for _ in range(number):
        name = input()
        unique_names.add(name)
    return unique_names


def print_results(data):
    [print(name) for name in data]


names_list = adding_new_names_from_input(int(input()))
print_results(names_list)
