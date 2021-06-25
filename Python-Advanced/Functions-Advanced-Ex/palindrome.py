def first_way_find_palindrome(data):
    half_len = len(data) // 2
    for index in range(half_len):
        left_char = data[index]
        right_char = data[len(data) - index - 1]
        if not left_char == right_char:
            return "Not palindrome"
    return "Is palindrome"


def second_way_find_palindrome(data, helper=0):
    if helper == len(data) // 2:
        return "Is palindrome"
    if not data[helper] == data[len(data) - helper - 1]:
        return "Not palindrome"
    return second_way_find_palindrome(data, helper + 1)


def third_way(data: iter, helper=0):
    data = list(data)
    if len(data) <= 1:
        return "Is palindrome"
    left_char = data.pop(0)
    right_char = data.pop(-1)
    if not left_char == right_char:
        return "Not palindrome"
    return third_way(data, helper + 1)


word = ""
print(first_way_find_palindrome(word))
print(second_way_find_palindrome(word))
print(third_way(word))
