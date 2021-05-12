input_data = input().split(", ")


if input_data[-1] == "wolf":
    print("Please go away and stop eating my sheep")
    exit()

input_data = list(reversed(input_data))

for index in range(1, len(input_data) + 1):
    if input_data[index] == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
        break
