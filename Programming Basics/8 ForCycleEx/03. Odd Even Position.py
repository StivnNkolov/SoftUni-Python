import sys

n = int(input())

sum_of_odds = 0
sum_of_even = 0
even_max = -sys.maxsize
even_min = sys.maxsize
odd_max = -sys.maxsize
odd_even = sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        sum_of_even += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        sum_of_odds += number
        if number > odd_max:
            odd_max = number
        if number < odd_even:
            odd_even = number


print(f"OddSum={sum_of_odds:.2f},")
if odd_even != sys.maxsize:
    print(f"OddMin={odd_even:.2f},")
else:
    print("OddMin=No,")
if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={sum_of_even:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")
if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")