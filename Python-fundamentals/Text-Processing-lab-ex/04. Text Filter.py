ban_list = input().split(", ")
text = input()
for word in ban_list:
    text = text.replace(word, ("*" * len(word)))

print(text)


