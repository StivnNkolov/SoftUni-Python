first_line = [int(num) for num in input().split()]
second_line = [int(num) for num in input().split()]
third_line = [int(num) for num in input().split()]

fourth_line = [first_line[0], second_line[0], third_line[0]]
fifth_line = [first_line[1], second_line[1], third_line[1]]
sixth_lie = [first_line[2], second_line[2], third_line[2]]
seventh_line = [first_line[2], second_line[1], third_line[0]]
eight_line = [first_line[0], second_line[1], third_line[2]]
all_shit = [first_line, second_line, third_line, fourth_line, fifth_line, sixth_lie, seventh_line, eight_line]

is_won = False

for wining_line in all_shit:
    if wining_line.count(1) == 3:
        print("First player won")
        is_won = True
        break
    if wining_line.count(2) == 3:
        print("Second player won")
        is_won = True
        break

if not is_won:
    print("Draw!")

