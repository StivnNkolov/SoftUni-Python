input_int = int(input())

for num in range(1, input_int + 1):
    num = str(num)
    current_sum = 0
    for element in range(len(num)):

        current_sum += int(num[element])
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
