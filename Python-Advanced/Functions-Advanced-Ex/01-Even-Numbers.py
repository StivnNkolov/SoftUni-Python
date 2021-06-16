# def even_number(number):
#     return number % 2 == 0
#
#
# def get_result(sequence):
#     even_nums = list((filter(even_number, sequence)))
#     return even_nums
#
#
# input_seq = [int(el) for el in input().split()]
# even_nums = get_result(input_seq)
#
# print(even_nums)


input_seq = map(int, input().split())

print(list(filter(lambda x: x % 2 == 0, input_seq)))
