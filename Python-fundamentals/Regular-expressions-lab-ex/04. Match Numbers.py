import re

input_data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = [obj.group() for obj in re.finditer(pattern, input_data)]
print(*valid_numbers)
