input_text = input()

try:
    input_number = int(input())
    print(input_text * input_number)
except ValueError:
    print("Variable times must be an integer")

