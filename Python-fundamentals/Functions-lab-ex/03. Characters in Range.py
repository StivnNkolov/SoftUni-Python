def finding_chars_in_range(ch1, ch2):
    needed_chars = ''
    for c in range(ord(ch1) + 1, ord(ch2)):
        needed_chars += chr(c) + " "
    return needed_chars


char1 = input()
char2 = input()

print(finding_chars_in_range(char1, char2))