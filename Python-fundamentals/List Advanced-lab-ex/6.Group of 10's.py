numbers = list(map(lambda x: int(x), input().split(", ")))

group = 10
max_num = max(numbers)

while numbers:
    my_list = []
    for num in numbers:
        if num in range(group - 10, group + 1):
            my_list.append(num)
    for num in my_list:
        numbers.remove(num)
    print(f"Group of {group}'s: {my_list}")
    group += 10
