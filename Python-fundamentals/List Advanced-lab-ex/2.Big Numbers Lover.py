numbers = input().split()

sorted_numbers = sorted(numbers, reverse=True)
sorted_numbers_as_int = [int(number) for number in sorted_numbers]
num_1 = "".join(sorted_numbers)

print(num_1)