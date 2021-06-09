input_heroes_names = input().split(", ")

dict_with_names_players = {key: {"items": [], "cost": 0} for key in input_heroes_names}

input_data = input()

while not input_data == "End":
    name, item, price = input_data.split("-")
    price = int(price)
    if item not in dict_with_names_players[name]["items"]:
        dict_with_names_players[name]["items"].append(item)
        dict_with_names_players[name]["cost"] += price

    input_data = input()

# for key, value in dict_with_names_players.items():
#     items_count = len(value["items"])
#     price = value["cost"]
#     print(f"{key} -> Items: {items_count}, Cost: {price}")

[print(f"{key} -> Items: {len(value['items'])}, Cost: {value['cost']}") for key, value in dict_with_names_players.items()]