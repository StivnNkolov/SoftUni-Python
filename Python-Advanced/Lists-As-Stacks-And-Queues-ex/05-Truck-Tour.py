from collections import deque

number_of_stops = int(input())

all_stops = deque(input() for stop in range(number_of_stops))


is_found = False

for big_circle_index in range(number_of_stops):
    petrol_in_tank = 0
    for small_circle in range(number_of_stops):
        current_stop = all_stops[small_circle].split()
        fuel = int(current_stop[0])
        distance = int(current_stop[1])
        petrol_in_tank += fuel
        if petrol_in_tank >= distance:
            petrol_in_tank -= distance
            if small_circle == len(all_stops)-1:
                print(big_circle_index)
                is_found = True
                break
        else:
            all_stops.append(all_stops.popleft())
            break
    if is_found:
        break
