substring = input()
input_string = input()

while substring in input_string:
    input_string = input_string.replace(substring, "")

print(input_string)
