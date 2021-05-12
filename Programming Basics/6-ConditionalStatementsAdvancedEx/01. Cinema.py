# Напишете програма, която чете тип прожекция (текст),
# брой редове и брой колони в залата (цели числа), въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

type_of_project = input()
columns = int(input())
rows = int(input())
ticket_price = 0

if type_of_project == "Premiere":
    ticket_price = 12
elif type_of_project == "Normal":
    ticket_price = 7.50
elif type_of_project == "Discount":
    ticket_price = 5
final_price = (columns * rows) * ticket_price
print(f"{final_price:.2f}")
