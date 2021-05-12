items_with_their_prices = input().split("|")
starting_budget = float(input())

budget_to_work_with = starting_budget
list_of_new_prices = []

for type_of_item in items_with_their_prices:
    item = type_of_item.split("->")[0]
    price = float(type_of_item.split("->")[1])
    if item == "Clothes" and budget_to_work_with >= price and price <= 50:
        budget_to_work_with -= price
        new_price = price + (price * 0.4)
        list_of_new_prices.append(new_price)
    elif item == "Shoes" and budget_to_work_with >= price and price <= 35:
        budget_to_work_with -= price
        new_price = price + (price * 0.4)
        list_of_new_prices.append(new_price)
    elif item == "Accessories" and budget_to_work_with >= price and price <= 20.50:
        budget_to_work_with -= price
        new_price = price + (price * 0.4)
        list_of_new_prices.append(new_price)


new_budget = sum(list_of_new_prices) + budget_to_work_with
profit = new_budget - starting_budget
# list_of_new_prices = [str(x) for x in list_of_new_prices]
# list_of_new_prices = [float(x) for x in list_of_new_prices]
for price in list_of_new_prices:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")