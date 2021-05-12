fires_with_their_cells = input().split("#")
water_amount = int(input())

effort = 0
total_fire = 0
putout_fires = []

for fire in fires_with_their_cells:
    current_fire = fire.split(" = ")[0]
    current_fire_value = int(fire.split(" = ")[1])
    if current_fire == "High" and 81 <= current_fire_value <= 125 and water_amount >= current_fire_value:
        water_amount -= current_fire_value
        total_fire += current_fire_value
        effort += 0.25 * current_fire_value
        putout_fires.append(current_fire_value)
    if current_fire == "Medium" and 51 <= current_fire_value <= 80 and water_amount >= current_fire_value:
        water_amount -= current_fire_value
        total_fire += current_fire_value
        effort += 0.25 * current_fire_value
        putout_fires.append(current_fire_value)
    if current_fire == "Low" and 1 <= current_fire_value <= 50 and water_amount >= current_fire_value:
        water_amount -= current_fire_value
        total_fire += current_fire_value
        effort += 0.25 * current_fire_value
        putout_fires.append(current_fire_value)


print(f"Cells:")
for putout in putout_fires:
    print(f" - {putout}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")