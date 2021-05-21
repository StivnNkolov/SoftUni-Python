from collections import deque

cups_capacity = deque([int(el) for el in input().split()])  # from the first entered cup
bottles_stored_capacity = deque([int(el) for el in input().split()])  # from the last received bottle

cups_queue = deque([])
while cups_capacity:
    cups_queue.append(cups_capacity.pop())

filled_cups = []

wasted_water = 0
have_bottles = True

while cups_queue:
    if bottles_stored_capacity:
        current_bottle = bottles_stored_capacity.pop()
        current_cup = cups_queue.pop()
        volume_to_be_filled = current_cup - current_bottle
        if volume_to_be_filled == 0:
            filled_cups.append(current_cup)
        elif volume_to_be_filled < 0:
            filled_cups.append(current_cup)
            wasted_water += abs(volume_to_be_filled)
        elif volume_to_be_filled > 0:
            if bottles_stored_capacity:
                volume_to_be_filled -= bottles_stored_capacity.pop()
                if volume_to_be_filled < 0:
                    filled_cups.append(current_cup)
                    wasted_water += abs(volume_to_be_filled)
                elif volume_to_be_filled == 0:
                    filled_cups.append(current_cup)
                else:

                    cups_queue.append(volume_to_be_filled)
            else:
                have_bottles = False
                break
    else:
        have_bottles = False
        break

if have_bottles:
    if not cups_queue:
        print(f"Bottles: {''.join([str(el) for el in bottles_stored_capacity])}")
        print(f"Wasted litters of water: {abs(wasted_water)}")
else:
    what_to_print = []
    while cups_queue:
        what_to_print.append(str(cups_queue.pop()))
    have_bottles = False
    print(f"Cups: {' '.join(what_to_print)}")
    print(f"Wasted litters of water: {wasted_water}")
