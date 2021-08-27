import functools


def vowel_filter(func):
    @functools.wraps
    def wrapper():
        vowels = ("aeiou" + "aeiou".upper())
        result = func()
        return [letter for letter in result if letter in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
