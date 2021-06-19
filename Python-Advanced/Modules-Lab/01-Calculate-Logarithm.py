from math import log

input_number = int(input())
base = input()

if base == "natural":
    print(f"{log(input_number):.2f}")
else:
    print(f"{log(input_number, int(base)):.2f}")