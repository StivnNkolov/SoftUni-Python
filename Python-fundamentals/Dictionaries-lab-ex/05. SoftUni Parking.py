number_of_commands = int(input())

currently_registered_plates = {}

for c_command in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username not in currently_registered_plates:
            currently_registered_plates[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == "unregister":
        username1 = command[1]
        if username1 not in currently_registered_plates:
            print(f"ERROR: user {username1} not found")
        else:
            currently_registered_plates.pop(username1)
            print(f"{username1} unregistered successfully")

for key, value in currently_registered_plates.items():
    print(f"{key} => {value}")
