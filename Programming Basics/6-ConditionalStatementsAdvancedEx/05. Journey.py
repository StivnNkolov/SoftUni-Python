# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# •	Бюджет - реално число;
# •	Един от двата възможни сезона - "summer” или "winter”.
budget = float(input())
season = input()

destination = ""
type_of_holiday = ""
money_spend = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_holiday = "Camp"
        money_spend = budget * 0.3
    elif season == "winter":
        type_of_holiday = "Hotel"
        money_spend = budget * 0.7
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_holiday = "Camp"
        money_spend = budget * 0.4
    elif season == "winter":
        type_of_holiday = "Hotel"
        money_spend = budget * 0.8
if budget > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        type_of_holiday = "Hotel"
        money_spend = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {money_spend:.2f}")
