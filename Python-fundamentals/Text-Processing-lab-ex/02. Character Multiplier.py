input_data = input().split()

left_side = input_data[0]
right_side = input_data[1]
remaining_char = ''

if len(left_side) > len(right_side):
    remaining_char = left_side[len(right_side):]
    left_side = left_side[:len(right_side)]
else:
    remaining_char += right_side[len(left_side):]
    right_side = right_side[:len(left_side)]

index = 0
total_sum = 0

while not index == len(left_side):
    total_sum += ord(left_side[index]) * ord(right_side[index])
    index += 1
for char in remaining_char:
    total_sum += ord(char)
    index += 1

print(total_sum)
