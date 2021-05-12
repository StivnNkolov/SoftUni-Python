import re
input_data = input()


pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"
# pattern = r'\b[A-Z]{1}[a-z]+\b \b[A-Z]{1}[a-z]+\b'
valid_names = re.findall(pattern, input_data)
print(*valid_names)