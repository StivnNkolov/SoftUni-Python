def adding_unique_names_to_set(names_count):
    unique_names_set = set()
    for _ in range(names_count):
        name = input()
        unique_names_set.add(name)
    return unique_names_set


def print_results(all_names):
    [print(el) for el in all_names]


unique_names = adding_unique_names_to_set(int(input()))
print_results(unique_names)
