input_data = input()

commands = input()

while not commands == "Generate":
    command = commands.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in input_data:
            print(f"{input_data} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        type = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if type == "Upper":
            substring = input_data[start_index:end_index]
            input_data = input_data.replace(substring, substring.upper())
            print(input_data)
        elif type == "Lower":
            substring = input_data[start_index:end_index]
            input_data = input_data.replace(substring, substring.lower())
            print(input_data)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        substring = input_data[start_index:end_index]
        input_data = input_data.replace(substring, "")
        print(input_data)
    commands = input()

print(f"Your activation key is: {input_data}")