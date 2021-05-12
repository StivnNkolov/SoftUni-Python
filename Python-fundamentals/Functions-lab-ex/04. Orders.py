def calculating_price(pName, pCount):
    if pName == "coffee":
        return pCount * 1.50
    elif pName == "water":
        return pCount * 1
    elif pName == "coke":
        return pCount * 1.4
    elif pName == "snacks":
        return pCount * 2


product = input()
product_count = int(input())

print(f"{calculating_price(product, product_count):.2f}")