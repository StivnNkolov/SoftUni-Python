book = input()

count = 0
searched_book = ""

text = input()
while text != book:
    if text != "No More Books":
        searched_book = text
        count += 1
    else:

        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break
    text = input()
if text == book:
    print(f"You checked {count} books and found it.")



# searched_book = input()
#
# books_count = 0
#
# book = input()
# while book != searched_book:
#     if book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {books_count} books.")
#         break
#     books_count += 1
#     book = input()
#
# if searched_book == book:
#     print(f"You checked {books_count} books and found it.")
