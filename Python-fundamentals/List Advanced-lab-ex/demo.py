days_for_the_trip = int(input())
whole_budget = float(input())
number_of_people = int(input())
price_for_fuel_for_kilometer = float(input())
food_exp_for_person_for_day = float(input())
price_for_room_for_one_person_for_one_night = float(input())

if number_of_people > 10:
    price_for_room_for_one_person_for_one_night -= price_for_room_for_one_person_for_one_night * 0.25

tottal_food_expences = (number_of_people * food_exp_for_person_for_day) * days_for_the_trip
total_price_for_hotel = (days_for_the_trip * number_of_people) * price_for_room_for_one_person_for_one_night
expences = tottal_food_expences + total_price_for_hotel

for day in range(1, days_for_the_trip + 1):
    travelled_distance = float(input())
    expences += travelled_distance * price_for_fuel_for_kilometer
    if day % 3 == 0 or day % 5 == 0:
        expences += 0.4 * expences
    elif day % 7 == 0:
        income = expences / number_of_people
        expences -= income
    if expences > whole_budget:
        print(f"Not enough money to continue the trip. You need {abs(whole_budget - expences):.2f}$ more.")
        break
if whole_budget >= expences:
    print(f"You have reached the destination. You have {abs(whole_budget - expences):.2f}$ budget left.")