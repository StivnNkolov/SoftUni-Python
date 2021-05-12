items_with_prices = input().split("|")
budget = float(input())

bought_items = []


for item in items_with_prices:
    name, price = item.split("->")
    price = float(price)
    if name == "Clothes":
        if price <= 50 and budget >= price:
            budget -= price
            bought_items.append(price)
    elif name == "Shoes":
        if price <= 35 and budget >= price:
            budget -= price
            bought_items.append(price)
    elif name == "Accessories":
        if price <= 20.50 and budget >= price:
            budget -= price
            bought_items.append(price)

new_prices = [(bought_items[b] * 0.4) + bought_items[b] for b in range(len(bought_items))]
profit = sum(new_prices) - sum(bought_items)
new_budget = budget + sum(new_prices)

for price in new_prices:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")