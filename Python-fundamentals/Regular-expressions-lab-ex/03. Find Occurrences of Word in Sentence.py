import re

input_txt = input()
searched_word = input()

pattern = rf"\b{searched_word}\b"

searched_word_count = re.findall(pattern, input_txt, re.IGNORECASE)
print(len(searched_word_count))
