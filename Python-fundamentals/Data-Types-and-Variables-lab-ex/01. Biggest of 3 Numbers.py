first = int(input())
second = int(input())
third = int(input())

if first > second and first > third:
    print(first)
elif second > third and second > first:
    print(second)
else:
    print(third)