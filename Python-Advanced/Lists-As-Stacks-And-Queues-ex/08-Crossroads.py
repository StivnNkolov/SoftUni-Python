from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

duration_of_green_light = int(input())
duration_of_the_free_window = int(input())

command = input()
cars_waiting_on_the_line = deque([])
crash = False
passed_cars = 0
while not command == END_COMMAND:
    if not command == GREEN_COMMAND:
        cars_waiting_on_the_line.append(command)
    else:
        needed_time_to_pass_for_car = 0
        initial_time_for_pass = duration_of_green_light
        free_window = duration_of_the_free_window
        while cars_waiting_on_the_line:
            if initial_time_for_pass == 0:
                break
            curr_car = cars_waiting_on_the_line.popleft()
            needed_time_to_pass_for_car = len(curr_car)
            initial_time_for_pass -= needed_time_to_pass_for_car
            if initial_time_for_pass == 0:
                passed_cars += 1
                break
            elif initial_time_for_pass < 0:
                free_window -= -initial_time_for_pass

                if free_window >= 0:
                    passed_cars += 1
                    free_window = duration_of_the_free_window
                    initial_time_for_pass = 0
                    continue
                else:
                    print("A crash happened!")
                    print(f"{curr_car} was hit at {curr_car[free_window]}.")
                    crash = True
                    break
            elif initial_time_for_pass > 0:
                passed_cars += 1
                continue
    if crash:
        break
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")

