def reverse_text(input_data: str):
    start_char = len(input_data) - 1

    while start_char >= 0:
        yield input_data[start_char]
        start_char -= 1


for char in reverse_text("step"):
    print(char, end='')
