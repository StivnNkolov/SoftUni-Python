import functools


def multiply(times):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(number):
            result = func(number) * times
            return result
        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

print(add_ten.__name__)
