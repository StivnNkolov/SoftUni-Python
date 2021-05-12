import re

input_data = input()
pattern = r"\d+"
numbers = []
while input_data:
    numbers.extend(re.findall(pattern, input_data))
    input_data = input()
print(*numbers)
