quantity = int(input())
days = int(input())

total_cost = 0
spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        spirit -= 20
        total_cost += tree_skirt + tree_garlands + tree_lights
        if day == days:
            spirit -= 30
    if day % 5 == 0:
        total_cost += quantity * tree_lights
        spirit += 17
    if day % 15 == 0:
        spirit += 30
    if day % 3 == 0:
        total_cost += (quantity * tree_skirt) + (quantity * tree_garlands)
        spirit += 13
    if day % 2 == 0:
        total_cost += quantity * ornament_set
        spirit += 5


print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")