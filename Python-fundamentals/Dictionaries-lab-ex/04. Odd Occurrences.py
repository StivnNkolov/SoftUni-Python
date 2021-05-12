words = [word.lower() for word in input().split()]

words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word] += 1

for key, value in words_count.items():
    if not value % 2 == 0:
        print(key, end=" ")



## softuni nachin

# words = input().split()
# dict = {}
#
# for word in words:
#     lower_word = word.lower()
#     if lower_word not in dict:
#         dict[lower_word] = 0
#     dict[lower_word] += 1
#
# for key, value in dict.items():
#     if value % 2 != 0:
#         print(key, end=" ")