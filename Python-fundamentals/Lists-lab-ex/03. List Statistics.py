number_of_lines = int(input())

positive_list = []
negative_list = []

for _ in range(number_of_lines):
    input_integer = int(input())
    if input_integer < 0:
        negative_list.append(input_integer)
    else:
        positive_list.append(input_integer)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")