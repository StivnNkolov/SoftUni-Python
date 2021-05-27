def search_for_element_in_matrix(searched_element, data):
    for r_index in range(len(data)):
        for c_index in range(len(data)):
            if searched_element == data[r_index][c_index]:
                return print(f"({r_index}, {c_index})")
    return print(f"{searched_element} does not occur in the matrix")


def create_matrix(number):
    m = []
    for input_row in range(number):
        m.append([])
        [m[input_row].append(el) for el in input()]
    return m


matrix = create_matrix(int(input()))
search_for_element_in_matrix(input(), matrix)
