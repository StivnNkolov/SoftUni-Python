input_numbers = [int(el) for el in input().split(", ")]
input_index = int(input())

working_dict = {index: input_numbers[index] for index in range(len(input_numbers))}
sorted_dict = sorted(working_dict.items(), key=lambda x: x[1])

clock_cycles = 0

for index, value in sorted_dict:
    clock_cycles += value
    if index == input_index:
        break

print(clock_cycles)
