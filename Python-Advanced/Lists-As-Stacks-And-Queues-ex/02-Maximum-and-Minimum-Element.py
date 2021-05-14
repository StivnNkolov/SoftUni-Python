from collections import deque


def check_if_initial_stack_is_empty(stack1):
    if stack1:
        return True
    return False


initial_stack = deque()

input_int = int(input())

for _ in range(input_int):
    input_data = input().split()
    query_num = input_data[0]
    if query_num == "1":
        value = int(input_data[1])
        initial_stack.append(value)
    elif query_num == "2":
        if check_if_initial_stack_is_empty(initial_stack):
            initial_stack.pop()
    elif query_num == "3":
        if check_if_initial_stack_is_empty(initial_stack):
            print(max(initial_stack))
    elif query_num == "4":
        if check_if_initial_stack_is_empty(initial_stack):
            print(min(initial_stack))

final_stack = deque()

for index in range(len(initial_stack)):
    final_stack.append(initial_stack.pop())

print(*final_stack, sep=", ")
