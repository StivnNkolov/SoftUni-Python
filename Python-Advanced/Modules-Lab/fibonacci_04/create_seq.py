def crete_fibonacci_seq(number):
    fibonacci = [0, 1]
    for num in range(number-2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
