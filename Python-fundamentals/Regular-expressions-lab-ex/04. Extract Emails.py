import re

input_data = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+?@[a-z]+\-?[a-z]+?(\.[a-z]+)+"

valid_emails = [obj.group() for obj in re.finditer(pattern, input_data)]
for email in valid_emails:
    print(email)

