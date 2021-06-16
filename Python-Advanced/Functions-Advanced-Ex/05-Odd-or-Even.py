def get_desired_sum(command, sequence):
    result = 0
    if command == "Even":
        result = sum(filter(lambda x: x % 2 == 0, sequence)) * len(sequence)
    elif command == "Odd":
        result = sum(filter(lambda x: x % 2 != 0, sequence)) * len(sequence)

    return result


input_command = input()
input_seq = [int(el) for el in input().split()]

print(get_desired_sum(input_command, input_seq))