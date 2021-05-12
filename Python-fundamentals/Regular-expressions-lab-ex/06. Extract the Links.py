import re

input_data = input()
pattern = r"[w]{3}\.[A-Za-z0-9\-]+\.[a-z]+((\.[a-z]+)+)?"
while input_data:
    valid_mail = [obj.group() for obj in re.finditer(pattern, input_data)]
    if valid_mail:
        print(*valid_mail)
    input_data = input()