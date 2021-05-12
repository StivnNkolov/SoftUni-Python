count_of_words = int(input())

dict_of_synonyms = {}

for _ in range(count_of_words):
    word = input()
    synonym = input()
    if word not in dict_of_synonyms:
        dict_of_synonyms[word] = [synonym]
    else:
        dict_of_synonyms[word].append(synonym)

for key, value in dict_of_synonyms.items():
    print(f"{key} - {', '.join(value)}")