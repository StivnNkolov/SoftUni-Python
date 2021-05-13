from collections import deque

# We create "constants" for the commands we can receive from the user's input
START_COMMAND = "Start"
END_COMMAND = "End"

ppl_waiting_for_water = deque()
water_amount = int(input())

# while loop to add people waiting for water in our queue until we receive start command
while True:
    input_data = input()
    if input_data == START_COMMAND:
        break
    else:
        ppl_waiting_for_water.append(input_data)

# another while loop to give water(if we have enough) or to refill the water
while True:
    command_input = input().split(" ")
    if command_input[0] == END_COMMAND:
        print(f"{water_amount} liters left")
        break
    elif command_input[0] == "refill":
        liters_to_add = int(command_input[1])
        water_amount += liters_to_add
    else:
        litters_to_give = int(command_input[0])
        if litters_to_give <= water_amount:
            print(f"{ppl_waiting_for_water.popleft()} got water")
            water_amount -= litters_to_give
        else:
            print(f"{ppl_waiting_for_water.popleft()} must wait")