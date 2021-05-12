budget = float(input())
price_for_kilo_brashno = float(input())

eggs_price = price_for_kilo_brashno * 0.75
milk_price_for_250 = ((price_for_kilo_brashno * 0.25) + price_for_kilo_brashno) / 4
price_for_one_cozonac = price_for_kilo_brashno + eggs_price + milk_price_for_250

cozonacs_made = 0
colored_eggs = 0


while not budget < price_for_one_cozonac:
    budget -= price_for_one_cozonac
    cozonacs_made += 1
    colored_eggs += 3
    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2

print(f"You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

