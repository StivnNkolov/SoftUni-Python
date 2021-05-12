import re

input_data = input()
pattern = r"\b(?P<Day>\d{2})(?P<Separator>/|\.|-)(?P<Month>[A-Z]{1}[a-z]{2})(?P=Separator)(?P<Year>\d{4})\b"
valid_dates = [obj.groupdict() for obj in re.finditer(pattern, input_data)]
for date in valid_dates:
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")
wekfhwkfh