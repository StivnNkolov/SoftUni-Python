def searching_for_smallest_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3


first_num = int(input())
second = int(input())
third = int(input())

print(searching_for_smallest_num(first_num, second, third))
