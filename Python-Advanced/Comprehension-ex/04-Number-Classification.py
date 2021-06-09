input_numbers = [int(num) for num in input().split(", ")]
# positive_nums = [str(num) for num in input_numbers if num >= 0]
# negative_nums = [str(num) for num in input_numbers if num < 0]
# even_nums = [str(num) for num in input_numbers if num % 2 == 0]
# odd_nums = [str(num) for num in input_numbers if not num % 2 == 0]

print(f"Positive: {', '.join(map(str, [num for num in input_numbers if num >= 0]))}")
print(f"Negative: {', '.join(map(str, [num for num in input_numbers if num < 0]))}")
print(f"Even: {', '.join(map(str, [num for num in input_numbers if num % 2 == 0]))}")
print(f"Odd: {', '.join(map(str, [num for num in input_numbers if not num % 2 == 0]))}")
