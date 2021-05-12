working_day_events = input().split("|")

energy = 100
coins = 100
is_done = True
max_energy = 100

for events in working_day_events:
    event = events.split("-")[0]
    value = int(events.split("-")[1])
    if event == "rest":
        gained = min(value, max_energy - energy)
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        coins -= value
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")

            break

if coins > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
