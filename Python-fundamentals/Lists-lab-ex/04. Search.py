number_of_lines = int(input())
searched_string = input()

initial_list = []
searched_list = []

for _ in range(number_of_lines):
    input_data = input()
    initial_list.append(input_data)
    if searched_string in input_data:
        searched_list.append(input_data)

print(initial_list)
print(searched_list)