rooms_count = int(input())

free_chairs = 0
rooms = 0
enough_chairs = True

for room in range(1, rooms_count + 1):
    input_data = input().split()
    chairs = input_data[0]
    taken_chairs = int(input_data[1])
    difference = abs((len(chairs)) - taken_chairs)
    if abs(len(chairs)) - taken_chairs < 0:
        print(f"{difference} more chairs needed in room {room}")
        enough_chairs = False
    else:
        free_chairs += difference

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")


