initial_string = input()
final_string = input()

current_string = ''
all_strings = [initial_string]


for index in range(1, len(initial_string) + 1):
    first_part = final_string[:index]
    second_part = initial_string[index:]
    current_string = first_part + second_part
    if current_string not in all_strings:
        print(current_string)
    all_strings.append(current_string)

