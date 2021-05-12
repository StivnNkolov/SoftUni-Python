# print("".join([char.replace(char, chr(ord(char) + 3)) for char in input()]))

# print("".join((list(map(lambda x: x.replace(x, chr(ord(x) + 3)), input())))))
#
# input_data = input()
#
# searched_data = ""
#
# for char in input_data:
#     current_char = chr(ord(char) + 3)
#     searched_data += current_char
# print(searched_data)

input_data = input()

encrypted_version = ''

for index in range(len(input_data)):
    encrypted_version += input_data[index].replace(input_data[index], chr(ord(input_data[index]) + 3))
print(encrypted_version)