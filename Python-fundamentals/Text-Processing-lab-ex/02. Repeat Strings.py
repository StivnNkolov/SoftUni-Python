input_data = input().split()

c_string = ""

for el in input_data:
    c_string += el * len(el)
print(c_string)


# print("".join([word * len(word) for word in input().split()]))
