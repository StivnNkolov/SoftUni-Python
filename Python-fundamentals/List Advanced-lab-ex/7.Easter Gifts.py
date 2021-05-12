starting_gift_list = input().split()

command = input()

while not command == "No Money":
    current_command = command.split()
    if current_command[0] == "OutOfStock":
        gift = current_command[1]
        for gif in starting_gift_list:
            if gift in starting_gift_list:
                desired_index = starting_gift_list.index(gift)
                starting_gift_list[desired_index] = "None"
    elif current_command[0] == "Required":
        gift = current_command[1]
        index = int(current_command[2])
        if index in range(len(starting_gift_list)):
            starting_gift_list[index] = gift
    elif current_command[0] == "JustInCase":
        gift = current_command[1]
        starting_gift_list[-1] = gift

    command = input()
print(" ".join(list(word for word in starting_gift_list if not word == "None")))


