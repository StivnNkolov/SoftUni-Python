# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

price_for_one_flower = 0
end_price = 0
first_price = 0

if type_of_flower == "Roses":
    if number_of_flowers > 80:
        first_price = number_of_flowers * 5
        end_price = first_price - (first_price * 0.1)
    else:
        end_price = number_of_flowers * 5
elif type_of_flower == "Dahlias":
    if number_of_flowers > 90:
        first_price = number_of_flowers * 3.80
        end_price = first_price - (first_price * 0.15)
    else:
        end_price = number_of_flowers * 3.80
elif type_of_flower == "Tulips":
    if number_of_flowers > 80:
        first_price = number_of_flowers * 2.80
        end_price = first_price - (first_price * 0.15)
    else:
        end_price = number_of_flowers * 2.80
elif type_of_flower == "Narcissus":
    if number_of_flowers < 120:
        first_price = number_of_flowers * 3
        end_price = first_price + (first_price * 0.15)
    else:
        end_price = number_of_flowers * 3
elif type_of_flower == "Gladiolus":
    if number_of_flowers < 80:
        first_price = number_of_flowers * 2.50
        end_price = first_price + (first_price * 0.2)
    else:
        end_price = number_of_flowers * 2.50
if budget - end_price >= 0:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {budget - end_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {end_price - budget:.2f} leva more.")