import re

input_data = input()

# pattern = r" ^|\+359( |-)2\1[0-9]{3}\1[0-9]{4}\b"
pattern = r" ^|\+359( |-)2\1\d{3}\1\d{4}\b"
valid_numbers = [object.group() for object in re.finditer(pattern, input_data)]
print(*valid_numbers, sep=", ")