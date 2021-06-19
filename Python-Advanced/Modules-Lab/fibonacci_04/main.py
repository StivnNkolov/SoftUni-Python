from fibonacci_04 import create_seq, locate_number_in_seq, constants

input_command = input()
seq = []
while not input_command == constants.STOP_COMMAND:
    input_command = input_command.split()
    if input_command[0] == constants.CREATE_COMMAND:
        count = int(input_command[2])
        seq = create_seq.crete_fibonacci_seq(count)
        print(*seq)
    elif input_command[0] == constants.LOCATE_COMMAND:
        number = int(input_command[1])
        locate_number_in_seq.check_for_number_in_seq(seq, number)

    input_command = input()
