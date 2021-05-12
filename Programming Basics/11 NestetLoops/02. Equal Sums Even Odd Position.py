first = int(input())
second = int(input())

for number in range(first, second + 1):
    count = 1
    even_sum = 0
    odd_sum = 0
    for digit in str(number):
        if count % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
        count += 1
    if even_sum == odd_sum:
        print(number, end=" ")
