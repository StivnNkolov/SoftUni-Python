# •	На първия ред е месецът – May, June, July, August, September или October;
# •	На втория ред е броят на нощувките – цяло число.
month = input()
stayovers = int(input())

apartment = 0
studio = 0
if month == "May" or month == "October":
    apartment = 65
    studio = 50
    if 7 < stayovers < 14:
        studio -= studio * 0.05
    elif stayovers > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    if stayovers > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
elif month == "July" or month == "August":
    apartment = 77
    studio = 76
    if stayovers > 14:
        apartment -= apartment * 0.1
print(f"Apartment: {stayovers * apartment:.2f} lv.")
print(f"Studio: {stayovers * studio:.2f} lv.")