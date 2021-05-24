def print_results(data):
    for el in data:
        ch, occurrence = el
        print(f"{ch}: {occurrence} time/s")


def sorting_elements_in_data(data):
    sorted_elements = sorted([el for el in data.items()])
    return sorted_elements


def counting_unique_elements(data):
    unique_elements = {}
    for char in data:
        if char not in unique_elements:
            unique_elements[char] = 0
        unique_elements[char] += 1
    return unique_elements


input_tuple = tuple(input())
unique_chars_in_input = set(input_tuple)
occurrences_dict = counting_unique_elements(unique_chars_in_input)
sorted_data = sorting_elements_in_data(occurrences_dict)
print_results(sorted_data)
