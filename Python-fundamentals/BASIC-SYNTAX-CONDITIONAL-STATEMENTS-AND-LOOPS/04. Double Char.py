# input_string = input()

# new_string = [(char * 2) for char in input_string]
# print(*[(char * 2) for char in input()], sep="")
# for char in input_string:
#     new_string += (char * 2)
#
# print(new_string)

print(*list(map(lambda x: (x * 2), input())), sep="")