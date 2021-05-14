input_data = input().split()


reversed_stack = []

for index in range(len(input_data)):
    reversed_stack.append(input_data.pop())

print(*reversed_stack)