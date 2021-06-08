# start_int = int(input())
# end_int = int(input())
#
# numbers = [el for el in range(start_int, end_int + 1)]
#
# divisors = [el for el in range(2, 11)]
#
# needed_numbers = []
# for num in numbers:
#     for divisor in divisors:
#         if num % divisor == 0:
#             needed_numbers.append(num)
#             break
#
# print(needed_numbers)
#
# print([el for el in range(start_int, end_int + 1) if [d for d in range(2, 11) if el % d == 0]])

def divisible(number):
    divisibleN = [num for num in range(2, 11) if number % num == 0]
    return True if divisibleN else False


start = int(input())
end = int(input())

print([num for num in range(start, end + 1) if divisible(num)])
