# import functools


def logged(funct):
    # @functools.wraps(funct)
    def wrapper(*args):
        result = funct(*args)
        string_result_from_decorator = f"you called {funct.__name__}{args}\nit returned {result}"
        return string_result_from_decorator

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
