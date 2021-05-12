def finding_perfect_number(number):
    sum_of_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_divisors += num
    if sum_of_divisors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


input_data = int(input())
print(finding_perfect_number(input_data))
