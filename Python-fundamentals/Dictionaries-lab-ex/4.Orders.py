product_prices = {}
product_count = {}

command = input()
while not command == "buy":
    product, price, count = command.split()
    price = float(price)
    count = int(count)
    if product not in product_count:
        product_count[product] = count
    else:
        product_count[product] += count
    product_prices[product] = price
    command = input()

for product in product_count:
    print(f"{product} -> {(product_count[product] * product_prices[product]):.2f}")