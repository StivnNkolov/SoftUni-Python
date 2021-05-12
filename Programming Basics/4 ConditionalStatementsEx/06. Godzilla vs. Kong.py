# Вход
# От конзолата се четат 3 реда:
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
number_of_statist = int(input())
money_for_one_statist = float(input())

money_for_decor = budget * 0.1 # cenata na dekora
budget_after_decor = budget - money_for_decor # budget ostavasht sled plashtane na dekor
money_for_all_statist = money_for_one_statist * number_of_statist # sumata nujna za vsichki statisti
if number_of_statist > 150:
    money_for_all_statist -= money_for_all_statist * 0.1
needed_money = money_for_decor + money_for_all_statist # nujnite pari za produkciqta
if needed_money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {needed_money - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - needed_money:.2f} leva left.")
