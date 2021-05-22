def print_results(parking_set):
    if not check_if_parking_is_empty(parking_set):
        for car in parking_set:
            print(car)
    else:
        print("Parking Lot is Empty")


def check_if_parking_is_empty(parking_set):
    if parking_set:
        return False
    return True


def adding_and_removing_cars(number):
    parking_info = set()
    for _ in range(number):
        car_info = tuple(input().split(", "))
        command, plate_number = car_info
        if command == "IN":
            parking_info.add(plate_number)
        else:
            parking_info.remove(plate_number)
    return parking_info


parking_details_set = adding_and_removing_cars(int(input()))
print_results(parking_details_set)
