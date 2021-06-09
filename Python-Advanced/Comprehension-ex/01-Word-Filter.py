input_data = input().split()
#
# for word in input_data:
#     if len(word) % 2 == 0:
#         print(word)


[print(el) for el in input_data if len(el) % 2 == 0]
