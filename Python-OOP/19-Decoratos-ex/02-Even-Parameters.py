def even_parameters(func):
    def wrapper(*args):
        initial_len = len(args)
        even_numbers_len = len([el for el in args if isinstance(el, int) and el % 2 == 0])
        if initial_len == even_numbers_len:
            result = func(*args)
            return result
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
