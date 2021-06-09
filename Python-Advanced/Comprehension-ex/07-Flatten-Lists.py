input_data = [el for el in input().split("|")][::-1]
new_list = [[num for num in el if num.isdigit()] for el in input_data if [num for num in el if num.isdigit()]]
print(*[" ".join(k) for k in new_list])

