# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число), въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.
product = input()
city = input()
quantity = float(input())
price = 0

# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	0.50	0.80	1.20	1.45	1.60
# Plovdiv	0.40	0.70	1.15	1.30	1.50
# Varna	0.45	0.70	1.10	1.35	1.55

if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50
elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
final_price = quantity * price
print(final_price)
