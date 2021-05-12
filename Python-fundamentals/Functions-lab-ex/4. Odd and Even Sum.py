def even_odd_calculator(num):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for digit in num_as_string:
        num_as_num = int(digit)
        if num_as_num % 2 == 0:
            even_sum += num_as_num
        else:
            odd_sum += num_as_num
    return even_sum, odd_sum



number = int(input())
even_result = even_odd_calculator(number)[0]
odd_result = even_odd_calculator(number)[1]
print(f"Odd sum = {odd_result}, Even sum = {even_result}")
