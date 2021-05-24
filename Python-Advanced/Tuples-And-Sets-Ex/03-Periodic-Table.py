def printing_results(data):
    [print(el) for el in data]


def creating_unique_el_set(number):
    chemical_comp_set = set()
    for _ in range(number):
        compounds = tuple(input().split())
        for item in compounds:
            chemical_comp_set.add(item)
    return chemical_comp_set


unique_el_sets = creating_unique_el_set(int(input()))
printing_results(unique_el_sets)
