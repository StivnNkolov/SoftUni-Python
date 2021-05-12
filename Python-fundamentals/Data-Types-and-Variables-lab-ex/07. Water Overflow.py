tank_capacity = 0

pours_count = int(input())

for pou in range(pours_count):
    pour = int(input())
    if tank_capacity + pour <= 255:
        tank_capacity += pour
    else:
        print(f"Insufficient capacity!")

print(tank_capacity)