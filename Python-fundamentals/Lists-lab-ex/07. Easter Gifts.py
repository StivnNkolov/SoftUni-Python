input_gifts = input().split()

commands = input()
while not commands == "No Money":
    commands = commands.split()
    if commands[0] == "OutOfStock":
        gift = commands[1]
        for index in range(len(input_gifts)):
            if input_gifts[index] == gift:
                input_gifts[index] = "None"
    elif commands[0] == "Required":
        gift1 = commands[1]
        index = int(commands[2])
        if 0 <= index < len(input_gifts):
            input_gifts[index] = gift1
    elif commands[0] == "JustInCase":
        gift2 = commands[1]
        input_gifts[-1] = gift2
    commands = input()

for gif in input_gifts:
    if not gif == "None":
        print(gif, end=" ")
