number_of_commands = int(input())

cars_in_the_parking_lot = set()

for _ in range(number_of_commands):
    car_info = tuple(input().split(", "))
    command, plate_number = car_info
    if command == "IN":
        cars_in_the_parking_lot.add(plate_number)
    else:
        if plate_number in cars_in_the_parking_lot:
            cars_in_the_parking_lot.remove(plate_number)


if cars_in_the_parking_lot:
    for car in cars_in_the_parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")
