input_data = input()

index = 0

while index < len(input_data) - 1:
    if input_data[index] == input_data[index + 1]:
        part_to_replace = input_data[index] + input_data[index + 1]
        input_data = input_data.replace(part_to_replace, input_data[index])
    else:
        index += 1
print(input_data)
