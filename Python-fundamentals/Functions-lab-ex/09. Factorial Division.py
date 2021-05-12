def factorial(number1):
    fact = 1
    for n in range(1, number1 + 1):
        fact *= n
    return fact


result = []

for number in range(2):
    num = int(input())
    result.append(factorial(num))
print(f"{result[0] / result[1]:.2f}")