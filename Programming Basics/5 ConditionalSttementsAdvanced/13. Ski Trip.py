days_for_stay = int(input())
type_of_room = input()
grade = input()
price_for_stayover = 0
if type_of_room == "room for one person":
    price_for_stayover = (days_for_stay - 1) * 18
elif type_of_room == "apartment":
    price_for_stayover = (days_for_stay - 1) * 25
    if days_for_stay < 10:
        price_for_stayover = price_for_stayover - (price_for_stayover * 0.3)
    elif 10 <= days_for_stay <= 15:
        price_for_stayover = price_for_stayover - (price_for_stayover * 0.35)
    elif days_for_stay > 15:
        price_for_stayover -= price_for_stayover * 0.5
elif type_of_room == "president apartment":
    price_for_stayover = (days_for_stay - 1) * 35
    if days_for_stay < 10:
        price_for_stayover -= price_for_stayover * 0.1
    elif 10 <= days_for_stay <= 15:
        price_for_stayover -= price_for_stayover * 0.15
    elif days_for_stay > 15:
        price_for_stayover -= price_for_stayover * 0.2
if grade == "positive":
    price_for_stayover += price_for_stayover * 0.25
elif grade == "negative":
    price_for_stayover -= price_for_stayover * 0.1
print(f"{price_for_stayover:.2f}")
