# input_data = input()
#
#
# while not input_data == "end":
#     reversed_word = ""
#     for char in range(len(input_data) - 1, -1, -1):
#         reversed_word += input_data[char]
#     print(reversed_word)
#     input_data = input()


input_data = input()

while not input_data == "end":
    print(f"{input_data} = {input_data[::-1]}")
    input_data = input()

