def print_first_part_of_triangle(number):
    for row in range(1, number + 1):
        for column in range(1, row + 1):
            print(column, end=" ")
        print()


def print_second_part_of_triangle(number):
    for row in range(number, 1, -1):
        for column in range(1, row):
            print(column, end=" ")
        print()


def create_triangle(number):
    print_first_part_of_triangle(number)
    print_second_part_of_triangle(number)
