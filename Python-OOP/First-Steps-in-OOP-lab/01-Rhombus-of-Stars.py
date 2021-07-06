def printing_output_a(size, curr_itt, char_to_print, end_of_the_line):
    for el in range(size - curr_itt):
        print(char_to_print, end=end_of_the_line)


def printing_output_b(curr_itt, char_to_print, end_of_the_line):
    for el in range(curr_itt):
        print(char_to_print, end=end_of_the_line)


input_size = int(input())

for first_part in range(1, input_size + 1):
    printing_output_a(input_size, first_part, char_to_print=" ", end_of_the_line="")
    printing_output_b(first_part, char_to_print="*", end_of_the_line=" ")
    print()

for second_part in range(1, input_size):
    printing_output_b(second_part, char_to_print=" ", end_of_the_line="")
    printing_output_a(input_size, second_part, char_to_print="*", end_of_the_line=" ")
    print()
