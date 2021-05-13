from collections import deque

input_data = input()

# using deque as stack
my_stack = deque()

# for loop to check if we have opening or closing bracket
for index in range(len(input_data)):

    # if input_data from index == ( we add the index of ( in our stack
    if input_data[index] == "(":
        my_stack.append(index)

    # if we input_data from index == )
    # we know that we have to print everything between our last ( and the ) that we found
    # we pop the last found ( and continue to search for the next ) or (
    if input_data[index] == ")":
        print(input_data[my_stack.pop():index + 1])
