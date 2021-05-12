# 1.	Цена на ягодите в лева – реално число;
# 2.	Количество на бананите в килограми – реално число;
# 3.	Количество на портокалите в килограми – реално число;
# 4.	Количество на малините в килограми – реално число;
# 5.	Количество на ягодите в килограми – реално число.

strawb_price = float(input())
bananas_weight = float(input())
oranges_weight = float(input())
berries_weight = float(input())
strawb_weight = float(input())

# •	цената на  малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.

berries_price = strawb_price / 2  # cenata na malinite za kilogram
oranges_price = berries_price - (berries_price * 0.4)  # cenata na portokalite za kilogram
bananas_price = berries_price - (berries_price * 0.8)  # cenata na bananite za kilogram

strawb_end_price = strawb_weight * strawb_price
bananas_end_price = bananas_price * bananas_weight
oranges_end_price = oranges_price * oranges_weight
berries_end_price = berries_price * berries_weight
print(strawb_end_price + bananas_end_price + oranges_end_price + berries_end_price)
