digits = ''
letters = ''
characters = ''

input_data = input()

for char in input_data:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    elif not char.isalnum():
        characters += char

print(digits)
print(letters)
print(characters)


# input_data = input()
#
# print("".join([number for number in input_data if number.isdigit()]))
# print("".join([letter for letter in input_data if letter.isalpha()]))
# print("".join([char for char in input_data if not char.isalnum()]))