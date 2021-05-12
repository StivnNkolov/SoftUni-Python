input_data = input()

capital_indexes = []

for index in range(len(input_data)):
    if input_data[index].isupper():
        capital_indexes.append(index)

print(capital_indexes)