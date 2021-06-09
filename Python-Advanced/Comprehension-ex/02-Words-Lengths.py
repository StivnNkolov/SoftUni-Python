input_data = input().split(", ")
#
# for name in input_data:
#     print(f"{name} -> {len(name)}")

print(*[f"{name} -> {len(name)}" for name in input_data], sep=", ")
