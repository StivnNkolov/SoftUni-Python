def print_results(data):
    [print(item) for item in data]


def creating_set(num):
    current_set = set()
    for _ in range(num):
        input_num = int(input())
        current_set.add(input_num)
    return current_set


def take_unique_items_in_sets(first, second):
    return first & second


n, m = tuple([int(el) for el in tuple(input().split())])

n_set = creating_set(n)
m_set = creating_set(m)
unique_items = take_unique_items_in_sets(n_set, m_set)
print_results(unique_items)
