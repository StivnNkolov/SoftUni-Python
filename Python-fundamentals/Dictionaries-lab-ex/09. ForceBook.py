users = {}

input_data = input()

while not input_data == "Lumpawaroo":
    if "|" in input_data:
        side, user = input_data.split(" | ")
        if user not in users:
            users[user] = side
    elif "->" in input_data:
        user, side = input_data.split(" -> ")
        if user not in users:
            users[user] = side
            print(f"{user} joins the {side} side!")
        else:
            users[user] = side
            print(f"{user} joins the {side} side!")
    input_data = input()

sides = {}

for key, value in users.items():
    if value not in sides:
        sides[value] = [key]
    else:
        sides[value].append(key)

sorted_sides = sorted(sides.items(), key=lambda kvs: (-len(kvs[1]), kvs[0]))

for key, value in sorted_sides:
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for s in sorted(value):
            print(f"! {s}")
