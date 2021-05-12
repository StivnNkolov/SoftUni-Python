input_data = input()
print(input_data)

for index in range(len(input_data)):
    if not input_data[index].isalnum():
        explosion_power = input_data[index + 1]
        explosion_power = int(explosion_power)
        for power in range(explosion_power):
            pass
