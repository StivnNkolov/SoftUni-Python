number_of_guests = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(number_of_guests):
    guest_number = input()
    if guest_number[0].isdigit():
        vip_guests.add(guest_number)
    else:
        regular_guests.add(guest_number)

guests_coming = input()
while not guests_coming == "END":
    if guests_coming in vip_guests:
        vip_guests.remove(guests_coming)
    elif guests_coming in regular_guests:
        regular_guests.remove(guests_coming)
    guests_coming = input()

missing_guests = regular_guests | vip_guests
sorted_missing_g = sorted(missing_guests)
print(len(sorted_missing_g))
for el in sorted_missing_g:
    print(el)
