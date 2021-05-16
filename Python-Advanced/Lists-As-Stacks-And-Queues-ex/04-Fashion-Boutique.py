from collections import deque

clothes_volumes = input().split()
racks_capacity = int(input())

my_stack = deque()

for garment in clothes_volumes:
    my_stack.append(garment)

used_racks = 0
current_space_taken = 0
while my_stack:
    current_piece = my_stack[-1]
    current_space_taken += int(current_piece)
    if current_space_taken < racks_capacity:
        if len(my_stack) == 1:
            used_racks += 1
            my_stack.pop()
        else:
            my_stack.pop()
    elif current_space_taken == racks_capacity:
        used_racks += 1
        current_space_taken = 0
        my_stack.pop()
    else:
        used_racks += 1
        current_space_taken = 0
print(used_racks)
