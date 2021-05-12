# normalno reshenie
input_data = input()
#
# new_list = []
#
# for number in input_data:
#     new_list.append(-(int(number)))
#
# print(new_list)

# reshenie s list comp.
# n_list = [-(int(num)) for num in input().split()]

# print([-(int(num)) for num in input().split()])

my_list = list([map(lambda x: -(int(x)), input_data)])
print(list(my_list))