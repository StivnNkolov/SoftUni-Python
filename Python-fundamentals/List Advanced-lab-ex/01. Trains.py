wagons_count = int(input())
wagon_list = [0] * wagons_count

command = input()
while not command == "End":
    my_command_as_list = command.split()
    if my_command_as_list[0] == "add":
        wagon_list[-1] += int(my_command_as_list[1])
    elif my_command_as_list[0] == "insert":
        wagon = int(my_command_as_list[1])
        people = int(my_command_as_list[2])
        wagon_list[wagon] += people
    elif my_command_as_list[0] == "leave":
        wagon = int(my_command_as_list[1])
        people = int(my_command_as_list[2])
        wagon_list[wagon] -= people
    command = input()
print(wagon_list)

