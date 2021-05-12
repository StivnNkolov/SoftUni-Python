input_integers = input().split(", ")
input_integers = [int(num) for num in input_integers]

new_list = []
zeros = []
for n in input_integers:
    if not n == 0:
        new_list.append(n)
    else:
        zeros.append(n)


for zero in zeros:
    new_list.append(zero)
print(new_list)