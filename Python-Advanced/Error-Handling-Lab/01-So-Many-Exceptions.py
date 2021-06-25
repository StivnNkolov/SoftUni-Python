# Input code below
# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)

# Fixes input code

numbers_list = input().split(", ")
result = 1

for number in numbers_list:
    number = int(number)
    if number <= 5:
        result *= number
    elif number > 5:
        result /= number

print(result)
