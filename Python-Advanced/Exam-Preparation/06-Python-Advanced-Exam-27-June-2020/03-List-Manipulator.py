def list_manipulator(sequence, *args):
    input_list = sequence
    first_command, second_command = args[:2]
    numbers = list(args[2:])

    if first_command == "add" and second_command == "beginning":
        return numbers + input_list
    elif first_command == "add" and second_command == "end":
        return input_list + numbers
    elif first_command == "remove" and second_command == "beginning":
        if numbers:
            return input_list[numbers[0]:]
        else:
            return input_list[1:]
    elif first_command == "remove" and second_command == "end":
        if numbers:

            return input_list[:len(input_list) - numbers[0]]
        else:
            input_list.pop()
            return input_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
