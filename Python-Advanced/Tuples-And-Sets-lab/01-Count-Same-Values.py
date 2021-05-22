# This is the wrong way to do it because you have 2 nested loops to get the result.
# square complexity
# user_input = [float(el) for el in input().split()]
#
# values_count = {}
#
# for el in user_input:
#     values_count[el] = user_input.count(el)
# print(values_count)

def print_result(count_dict):
    for key, value in count_dict.items():
        print(f"{float(key)} - {value} times")


def collecting_chars_count(input_list):
    values_count_dict = {}
    for ch in input_list:
        if ch not in values_count_dict:
            values_count_dict[ch] = 0
        values_count_dict[ch] += 1
    return values_count_dict


input_values = input().split()
data_dict = collecting_chars_count(input_values)
print_result(data_dict)
