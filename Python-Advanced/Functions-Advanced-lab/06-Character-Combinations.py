from itertools import permutations


# def char_combinations(text, index=0):
#     if index == len(text):
#         print("".join(text))
#         return
#
#     for i in range(index, len(text)):
#         text[index], text[i] = text[i], text[index]
#         char_combinations(text, index + 1)
#         text[index], text[i] = text[i], text[index]
#
#
# input_string = list(input())
# char_combinations(input_string)

input_text = list(input())
[print(*el, sep="") for el in permutations(input_text)]