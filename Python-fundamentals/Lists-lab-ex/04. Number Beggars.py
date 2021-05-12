list_of_amounts = input().split(", ")
number_of_beggars = int(input())

sums_list = []

for beggar in range(number_of_beggars):
    each_beggar_amount = 0
    for index in range(beggar, len(list_of_amounts), number_of_beggars):
        each_beggar_amount += int(list_of_amounts[index])
    sums_list.append(each_beggar_amount)

print(sums_list)