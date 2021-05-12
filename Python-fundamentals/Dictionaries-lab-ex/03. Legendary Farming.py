important_items = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

# own_legendary_item = False
# while not own_legendary_item:
#     input_data = input().split()
#     for index in range(0, len(input_data), 2):
#         key = input_data[index + 1].lower()
#         value = int(input_data[index])
#         if key == "shards":
#             important_items[key] += value
#             if important_items[key] >= 250:
#                 important_items[key] -= 250
#                 print(f"Shadowmourne obtained!")
#                 own_legendary_item = True
#                 break
#         elif key == "fragments":
#             important_items[key] += value
#             if important_items[key] >= 250:
#                 important_items[key] -= 250
#                 print(f"Valanyr obtained!")
#                 own_legendary_item = True
#                 break
#         elif key == "motes":
#             important_items[key] += value
#             if important_items[key] >= 250:
#                 important_items[key] -= 250
#                 print(f"Dragonwrath obtained!")
#                 own_legendary_item = True
#                 break
#         else:
#             if key not in junk:
#                 junk[key] = value
#             else:
#                 junk[key] += value
# sorted_import_items = sorted(important_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
# for key, value in sorted_import_items:
#     print(f"{key}: {value}")
#
# sorted_junk = sorted(junk.items(), key=lambda x: x[0])
# for key, value in sorted_junk:
#     print(f"{key}: {value}")

## gornoto po mi haresva to e moe
own_legendary_item = False
while not own_legendary_item:
    input_data = input().split()
    for index in range(0, len(input_data), 2):
        key = input_data[index + 1].lower()
        value = int(input_data[index])
        if key == "shards" or key == "fragments" or key == "motes":
            important_items[key] += value
            if important_items["shards"] >= 250:
                important_items["shards"] -= 250
                print("Shadowmourne obtained!")
                own_legendary_item = True
                break
            elif important_items["fragments"] >= 250:
                important_items["fragments"] -= 250
                print("Valanyr obtained!")
                own_legendary_item = True
                break
            elif important_items["motes"] >= 250:
                important_items["motes"] -= 250
                print("Dragonwrath obtained!")
                own_legendary_item = True
                break
        else:
            if key not in junk:
                junk[key] = value
            else:
                junk[key] += value

for key, value in sorted(important_items.items(), key=lambda kvs: (-kvs[1], kvs[0])):
    print(f"{key}: {value}")

for key, value in sorted(junk.items(), key=lambda kvs: kvs[0]):
    print(f"{key}: {value}")

