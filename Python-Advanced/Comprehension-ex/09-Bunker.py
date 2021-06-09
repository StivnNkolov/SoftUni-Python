input_item_categories = input().split(", ")

categories_dict = {category: [] for category in input_item_categories}
end_quantity = 0
end_quality = 0

input_number = int(input())

for _ in range(input_number):
    cat, item_name, values = input_data = input().split(" - ")
    quantity, quality = values.split(";")
    quantity_value = int(quantity.split(":")[1])
    quality_value = int(quality.split(":")[1])
    categories_dict[cat].append(item_name)
    end_quantity += quantity_value
    end_quality += quality_value

print(f"Count of items: {end_quantity}")
print(f"Average quality: {end_quality / len(input_item_categories):.2f}")
# for key, value in categories_dict.items():
#     print(f"{key} -> {', '.join(value)}")


[print(f"{key} -> {', '.join(value)}") for key, value in categories_dict.items()]
