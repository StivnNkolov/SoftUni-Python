user_input = [float(el) for el in input().split()]
unique_numbers = set(user_input)
users_tuple = tuple(user_input)

for el in users_tuple:
    if el in unique_numbers:
        print(f"{el} - {users_tuple.count(el)} times")
        unique_numbers.discard(el)
