working_day_events = input().split("|")


energy = 100
coins = 100
is_closed = False

for event in working_day_events:
    action, value = event.split("-")
    value = int(value)
    if action == "rest":
        if energy + value > 100:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.")
        else:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
            continue
        else:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
    else:
        if coins - value <= 0:
            print(f"Closed! Cannot afford {action}.")
            is_closed = True
            break
        else:
            coins -= value
            print(f"You bought {action}.")

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
