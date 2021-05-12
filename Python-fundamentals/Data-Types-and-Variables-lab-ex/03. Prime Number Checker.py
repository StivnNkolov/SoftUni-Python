input_data = int(input())

divisor_count = 0

for divisor in range(1, input_data + 1):
    if input_data % divisor == 0:
        divisor_count += 1

if divisor_count == 2:
    print("True")
else:
    print("False")