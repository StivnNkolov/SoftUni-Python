def characters_in_between(first_char, second_char):
    list_with_chars_in_between = []
    for i in range(ord(first_char) + 1, ord(second_char)):
        list_with_chars_in_between.append(chr(i))
    return list_with_chars_in_between


char1 = input()
char2 = input()
result = characters_in_between(char1, char2)
print(" ".join(result))
