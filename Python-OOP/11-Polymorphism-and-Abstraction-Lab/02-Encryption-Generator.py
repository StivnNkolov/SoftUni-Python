class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = ''
        for character in self.text:
            ch_number = ord(character) + other
            if ch_number < 32:
                ch_number += 95
            if ch_number > 126:
                ch_number -= 95

            result += chr(ch_number)
        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))





