input_data = input()

products_dict = {}

while not input_data == "statistics":
    product, count = input_data.split(": ")
    count = int(count)
    if product in products_dict:
        products_dict[product] += count
    else:
        products_dict[product] = count
    input_data = input()

print("Products in stock:")
for product, count in products_dict.items():
    print(f"- {product}: {count}")

print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")
