n = int(input())

count = 1
is_bigger = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if count > n:
            is_bigger = True
            break
        print(f"{count}", end=" ")
        count += 1
    if is_bigger:
        break
    print()

