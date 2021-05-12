number_of_lines = int(input())

string = ''

for line in range(number_of_lines):
    input_data = input()
    if "(" in input_data or ")" in input_data:
        string += input_data

if string.startswith(")"):
    print("UNBALANCED")
elif "((" in string:
    print("UNBALANCED")
elif "))" in string:
    print("UNBALANCED")
else:
    print("BALANCED")
