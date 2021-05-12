number = int(input())

for n in range(1, number + 1):
    print("*" * n)
for j in range(number - 1, 0, -1):
    print("*" * j)
