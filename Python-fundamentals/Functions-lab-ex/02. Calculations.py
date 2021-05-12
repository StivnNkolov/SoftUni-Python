def calculator(input_operator, num1, num2):
    if input_operator == 'multiply':
        return num1 * num2
    elif input_operator == 'divide':
        return num1 // num2
    elif input_operator == 'add':
        return num1 + num2
    elif input_operator == 'subtract':
        return num1 - num2


operator = input()
first_int = int(input())
second_int = int(input())

print(calculator(operator, first_int, second_int))