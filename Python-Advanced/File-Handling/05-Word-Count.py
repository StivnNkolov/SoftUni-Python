with open("words.txt", "r") as file:
    words_to_count = [el.lower() for el in file.read().split()]

with open("01text.txt") as file:
    text_we_work_with = [el.lower().lstrip("-").rstrip("?!.,") for el in file.read().split()]

dict_with_counts = {}
for el in words_to_count:
    dict_with_counts[el] = text_we_work_with.count(el)

sorted_dict = sorted(dict_with_counts.items(), key=lambda x: -x[1])
for word, count in sorted_dict:
    print(f"{word} - {count}")