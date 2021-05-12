# 1.	Броят на дните, в които тече кампанията – цяло число;
# 2.	Броят на сладкарите – цяло число;
# 3.	Броят на тортите – цяло число;
# 4.	Броят на гофретите – цяло число;
# 5.	Броят на палачинките – цяло число.
# •	парите, които са събрани.
# 1/8 от крайната сума ще бъде използвана за покриване на разходите
# •	Торта - 45 лв.
# •	Гофрета - 5.80 лв.
# •	Палачинка – 3.20 лв.


days_for_the_campaign = int(input())
number_of_coocks = int(input())
cakes = int(input()) #za edin gotvach za edin den
gofreti = int(input()) #za edin gotvach za edin den
pancakes = int(input()) #za edin gotvach za edin den

cakes_money_from_one_day = cakes * 45   #sumata koqto izkarva edin gotva` za edin den ot torti
gofreti_money_for_one_day = gofreti * 5.80  ##sumata koqto izkarva edin gotva` za edin den ot torti
pancake_money_for_one_day = pancakes * 3.20     #sumata koqto izkarva edin gotva` za edin den ot torti
money_for_one_day_from_one_cook = cakes_money_from_one_day + gofreti_money_for_one_day + pancake_money_for_one_day
money_for_all_coocks_one_day = money_for_one_day_from_one_cook * number_of_coocks
money_from_all_coocks_FOR_all_days = money_for_all_coocks_one_day * days_for_the_campaign
money_after_costs = money_from_all_coocks_FOR_all_days - (money_from_all_coocks_FOR_all_days / 8)
print(money_after_costs)


