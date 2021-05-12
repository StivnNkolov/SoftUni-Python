lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_b_count = 0
sword_b_count = 0
shield_b_count = 0
armor_b_count = 0

for fight in range(1, lost_fight_count + 1):
    if fight % 2 == 0:
        helmet_b_count += 1
    if fight % 3 == 0:
        sword_b_count += 1
    if fight % 6 == 0:
        shield_b_count += 1
        if shield_b_count % 2 == 0:
            armor_b_count += 1

expenses = (helmet_b_count * helmet_price) + (sword_b_count * sword_price) + (shield_b_count * shield_price) + (armor_b_count * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")