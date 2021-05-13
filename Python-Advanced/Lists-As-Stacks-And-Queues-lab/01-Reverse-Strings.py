from collections import deque

input_string = input()

# we use deque for our stack because its faster than using list
my_stack = deque()

# the two for loops are example of stack mechanism. LAST IN FIRST OUT
# for loop to fill our stack from our input
for ch in input_string:
    my_stack.append(ch)


reversed_string = ''

# for loop to create our reversed input.
for index in range(len(my_stack)):
    reversed_string += my_stack.pop()

print(reversed_string)
