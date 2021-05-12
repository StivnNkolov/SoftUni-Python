# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,  намира
# най-голямото измежду тях и го принтира.
# Въвежда се по едно число на ред.
import sys

number = input()

max_number = -sys.maxsize

while number != "Stop":
    if int(number) > max_number:
        max_number = int(number)
    number = input()

print(f"{max_number}")