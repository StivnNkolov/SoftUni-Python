def print_results(odd_sum, even_sum, odd_data, even_data):
    if odd_sum == even_sum:
        print(", ".join([str(el) for el in odd_data | even_data]))
    elif odd_sum > even_sum:
        print(", ".join([str(el) for el in odd_data - even_data]))
    elif even_sum > odd_sum:
        print(", ".join([str(el) for el in odd_data ^ even_data]))


def taking_sets_sum(odd, even):
    return sum(odd), sum(even)


def creating_even_odd_data(input_number):
    odd_set = set()
    even_set = set()
    for number in range(1, input_number + 1):
        input_name = tuple(input())
        value_behind_name = 0
        divided_value = 0
        for ch in input_name:
            value_behind_name += ord(ch)
            divided_value = value_behind_name // number
        if divided_value % 2 == 0:
            even_set.add(divided_value)
        else:
            odd_set.add(divided_value)
    return odd_set, even_set


odd_set, even_set = creating_even_odd_data(int(input()))
odd_sum, even_sum = taking_sets_sum(odd_set, even_set)
print_results(odd_sum, even_sum, odd_set, even_set)
