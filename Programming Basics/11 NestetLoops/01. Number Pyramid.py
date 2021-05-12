n = int(input())
number = 1
is_bigger = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if number > n:
            is_bigger = True
            break
        print(number, end=" ")
        number += 1
    if is_bigger:
        break
    print()