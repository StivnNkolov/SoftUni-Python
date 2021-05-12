import sys
n = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(n):
    number = int(input())
    if max_number < number:
        max_number = number
    if min_number > number:
        min_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")