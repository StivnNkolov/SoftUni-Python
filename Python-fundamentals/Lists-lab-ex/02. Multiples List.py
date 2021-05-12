factor = int(input())
count = int(input())
#
# my_list = []
#
# for _ in range(1, count + 1):
#     my_list.append(factor * _)
#
# print(my_list)


print([(factor * num) for num in range(1, count + 1)])