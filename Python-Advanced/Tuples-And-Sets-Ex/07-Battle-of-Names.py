number_of_names = int(input())

odd_set = set()
even_set = set()

for _ in range(1, number_of_names + 1):
    input_name = tuple(input())
    value_behind_name = 0
    divided_value = 0
    for ch in input_name:
        value_behind_name += ord(ch)
        divided_value = value_behind_name // _
    if divided_value % 2 == 0:
        even_set.add(divided_value)
    else:
        odd_set.add(divided_value)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if odd_sum == even_sum:
    print(", ".join([str(el) for el in odd_set | even_set]))
elif odd_sum > even_sum:
    print(", ".join([str(el) for el in odd_set - even_set]))
elif even_sum > odd_sum:
    print(", ".join([str(el) for el in odd_set ^ even_set]))

