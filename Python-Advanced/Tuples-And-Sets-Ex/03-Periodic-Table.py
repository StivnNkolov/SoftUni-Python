number_of_input = int(input())

chemical_comp_set = set()

for _ in range(number_of_input):
    compounds = tuple(input().split())
    for item in compounds:
        chemical_comp_set.add(item)

[print(item) for item in chemical_comp_set]
