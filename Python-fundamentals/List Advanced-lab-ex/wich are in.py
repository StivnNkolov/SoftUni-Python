first_list = input().split(", ")
second_list = input().split(", ")

searched_list = []

for words in first_list:
    for word in second_list:
        if words in word:
            searched_list.append(words)
print(sorted(set(searched_list), key=searched_list.index))

