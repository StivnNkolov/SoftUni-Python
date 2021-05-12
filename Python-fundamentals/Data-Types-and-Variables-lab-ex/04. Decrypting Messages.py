key = int(input())

number_of_lines = int(input())

message = ''

for c in range(number_of_lines):
    char = input()
    message += chr(ord(char) + key)

print(message)