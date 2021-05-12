food_and_quanities = input().split()

food_dict = {}

for index in range(0, len(food_and_quanities), 2):
    key_food = food_and_quanities[index]
    value_food = int(food_and_quanities[index + 1])
    food_dict[key_food] = value_food

print(food_dict)
