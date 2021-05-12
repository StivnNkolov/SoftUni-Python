# От конзолата се четат три реда:
# •	Бюджет на групата – цяло число;
# •	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари – цяло число.
budget = int(input())
season = input()
number_fisherman = int(input())

price_for_the_ship = 0

if season == "Spring":
    price_for_the_ship = 3000
    if number_fisherman <= 6:
        price_for_the_ship -= price_for_the_ship * 0.1
    elif 7 < number_fisherman <= 11:
        price_for_the_ship -= price_for_the_ship * 0.15
    elif number_fisherman > 12:
        price_for_the_ship -= price_for_the_ship * 0.25
elif season == "Summer" or season == "Autumn":
    price_for_the_ship = 4200
    if number_fisherman <= 6:
        price_for_the_ship -= price_for_the_ship * 0.1
    elif 7 < number_fisherman <= 11:
        price_for_the_ship -= price_for_the_ship * 0.15
    elif number_fisherman > 12:
        price_for_the_ship -= price_for_the_ship * 0.25
elif season == "Winter":
    price_for_the_ship = 2600
    if number_fisherman <= 6:
        price_for_the_ship -= price_for_the_ship * 0.1
    elif 7 < number_fisherman <= 11:
        price_for_the_ship -= price_for_the_ship * 0.15
    elif number_fisherman > 12:
        price_for_the_ship -= price_for_the_ship * 0.25
if number_fisherman % 2 == 0 and season != "Autumn":
    price_for_the_ship -= price_for_the_ship * 0.05
if budget - price_for_the_ship >= 0:
    print(f"Yes! You have {budget - price_for_the_ship:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_for_the_ship - budget:.2f} leva.")