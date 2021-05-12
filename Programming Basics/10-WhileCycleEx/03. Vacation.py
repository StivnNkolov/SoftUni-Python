# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.

price_for_excursion = float(input())
owned_money = float(input())

all_days = 0
spending_counter = 0

while owned_money < price_for_excursion and spending_counter < 5:
    command = input()
    amount = float(input())
    all_days += 1
    if command == "save":
        owned_money += amount
        spending_counter = 0
    elif command == "spend":
        owned_money -= amount
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0
if spending_counter == 5:
    print("You can't save the money.")
    print(all_days)
elif owned_money >= price_for_excursion:
    print(f"You saved the money for {all_days} days.")