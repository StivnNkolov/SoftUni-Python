age = int(input())
washer = float(input())
toy_price = int(input())

saved_money = 0

for years in range(1, age + 1):
    if years % 2 == 0:
        saved_money += (years * 10 / 2) - 1
    else:
        saved_money += toy_price

if saved_money >= washer:
    print(f"Yes! {abs(washer - saved_money):.2f}")
else:
    print(f"No! {abs(saved_money - washer):.2f}")
