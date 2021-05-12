def add_and_subtract(num1, num2, num3):
    def sum_numbers():
        return num1 + num2

    def subtract():
        needed_num = sum_numbers()
        return needed_num - num3

    return subtract()


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))