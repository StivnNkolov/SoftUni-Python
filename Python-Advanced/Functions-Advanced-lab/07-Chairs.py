# from itertools import combinations
#
# input_data = input().split(", ")
# number_of_chairs = int(input())
#
# [print(*el, sep=", ") for el in combinations(input_data, number_of_chairs)]
#

def combinations(data, number, comb=[]):
    if number == len(comb):
        print(*comb)
        return
    for index in range(len(data)):
        curr_el = data[index]
        comb.append(curr_el)
        combinations(data[index + 1:], number, comb)
        comb.pop()


input_names = input().split(", ")
number_of_chairs = int(input())
# combinations(input_names, number_of_chairs)
