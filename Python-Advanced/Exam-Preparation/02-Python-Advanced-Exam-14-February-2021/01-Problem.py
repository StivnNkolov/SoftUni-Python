from collections import deque

fire_work_effects = deque(int(el) for el in input().split(", ") if int(el) > 0)
explosives_power = deque(int(el) for el in input().split(", ") if int(el) > 0)

palm_firework = 0
willow_firework = 0
cross_firework = 0
ran_out_of_material = False

while palm_firework < 3 or willow_firework < 3 or cross_firework < 3:
    if fire_work_effects and explosives_power:
        current_firework = fire_work_effects.popleft()
        current_explosive = explosives_power.pop()
        current_value = current_firework + current_explosive
        if current_value % 3 == 0 and current_value % 5 != 0:
            palm_firework += 1
        elif current_value % 3 != 0 and current_value % 5 == 0:
            willow_firework += 1
        elif current_value % 3 == 0 and current_value % 5 == 0:
            cross_firework += 1

        else:
            current_firework -= 1
            if current_firework > 0:
                fire_work_effects.append(current_firework)
            explosives_power.append(current_explosive)
    else:
        ran_out_of_material = True
        break

if not ran_out_of_material:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fire_work_effects:
    print(f"Firework Effects left: {', '.join(map(str, fire_work_effects))}")
if explosives_power:
    print(f"Explosive Power left: {', '.join(map(str, explosives_power))}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {cross_firework}")
