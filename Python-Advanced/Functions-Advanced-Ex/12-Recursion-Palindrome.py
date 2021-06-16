def palindrome(string, index):
    index_for_end = len(string) // 2
    if index == index_for_end:
        return f"{string} is a palindrome"
    if not string[index] == string[len(string)- index - 1]:
        return f"{string} is not a palindrome"
    return palindrome(string, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
