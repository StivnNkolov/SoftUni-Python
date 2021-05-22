def print_results(data):
    sorted_data = sorting_output(data)
    print(len(sorted_data))
    [print(el) for el in sorted_data]


def sorting_output(data):
    return sorted(data)


def adding_to_reservations(number):
    vip_guests = set()
    regular_guests = set()

    for guest in range(number):
        reservation = input()
        if reservation[0].isdigit():
            vip_guests.add(reservation)
        else:
            regular_guests.add(reservation)
    return vip_guests, regular_guests


def removing_guests_from_list(vip, regular):
    guest = input()
    while not guest == "END":
        if guest in vip:
            vip.remove(guest)
        elif guest in regular:
            regular.remove(guest)
        guest = input()
    missing_guests = regular | vip
    return missing_guests


vip_list, regular_list = adding_to_reservations(int(input()))
missing_guests_list = removing_guests_from_list(vip_list, regular_list)
print_results(missing_guests_list)
