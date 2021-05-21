input_tuple = tuple(input())

unique_chars_in_input = set(input_tuple)

occurrences_dict = {}

for char in unique_chars_in_input:
    occurrences_dict[char] = input_tuple.count(char)

sorted_dict = sorted([(key, value) for (key, value) in occurrences_dict.items()])
for el in sorted_dict:
    ch, occurrences = el
    print(f"{ch}: {occurrences} time/s")
