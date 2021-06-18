import os

END_COMMAND = "End"
CREATE_COMMAND = "Create"
ADD_COMMAND = "Add"
REPLACE_COMMAND = "Replace"
DELETE_COMMAND = "Delete"

input_command = input()

while not input_command == END_COMMAND:
    current_command_with_param = input_command.split("-")
    command = current_command_with_param[0]
    if command == CREATE_COMMAND:
        new_file_name = current_command_with_param[1]
        with open(new_file_name, "w") as file:
            input_command = input()
            continue
    elif command == ADD_COMMAND:
        file_name = current_command_with_param[1]
        content_to_append = current_command_with_param[2]
        with open(file_name, "a") as file1:
            file1.writelines(content_to_append + "\n")
    elif command == REPLACE_COMMAND:
        file_name1 = current_command_with_param[1]
        try:
            with open(file_name1, "r") as file2:
                old_string = current_command_with_param[2]
                new_string = current_command_with_param[3]
                text = file2.read()
                text = text.replace(old_string, new_string)
            with open(file_name1, "w") as file3:
                file3.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif command == DELETE_COMMAND:
        file_name2 = current_command_with_param[1]
        try:
            os.remove(file_name2)
        except FileNotFoundError:
            print("An error occurred")

    input_command = input()
