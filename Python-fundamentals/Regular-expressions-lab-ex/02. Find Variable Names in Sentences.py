import re

input_data = input()

pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+\b"

valid_names = [obj.group() for obj in re.finditer(pattern, input_data)]
print(*valid_names, sep=",")