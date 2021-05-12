all_fires_info = input().split("#")
water = int(input())

cells = []
effort = 0
total_fire = 0

for fire in all_fires_info:
    type_of_fire, value = fire.split(" = ")
    value = int(value)
    if type_of_fire == "High" and 81 <= value <= 125:
        if water < value:
            continue
        else:
            water -= value
            effort += value * 0.25
            cells.append(value)
            total_fire += value
    elif type_of_fire == "Medium" and 51 <= value <= 80:
        if water < value:
            continue
        else:
            water -= value
            effort += value * 0.25
            cells.append(value)
            total_fire += value
    elif type_of_fire == "Low" and 1 <= value <= 50:
        if water < value:
            continue
        else:
            water -= value
            effort += value * 0.25
            cells.append(value)
            total_fire += value

print(f"Cells:")
for c in cells:
    print(f" - {c}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")