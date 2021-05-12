input_data = input()

new_line = "\n"
print(new_line.join(
    [input_data[char] + input_data[char + 1] for char in range(len(input_data)) if input_data[char] == ":"]))

# for char in range(len(input_data)):
#     if input_data[char] == ":":
#         print(input_data[char] + input_data[char + 1])
