# Initial code

# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page


# Refactored code

class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0


class TurnBookPage:
    def __init__(self, b: Book, wanted_page):
        self.book = b
        self.wanted_page = wanted_page

    @property
    def wanted_page(self):
        return self.__wanted_page

    @wanted_page.setter
    def wanted_page(self, value):
        if not isinstance(value, int) or value == self.book.page or value < 0:
            raise Exception("Wrong input for wanted page")
        self.__wanted_page = value

    def turn_page(self):
        self.book.page = self.wanted_page


book = Book("Raw", "Dostoevski", "At the desk")
print(f"Book name: {book.title}, Author: {book.author}, Book location: {book.location}, Page we need: {book.page}")
turn_page = TurnBookPage(book, 2)
turn_page.turn_page()


print(f"Book name: {book.title}, Author: {book.author}, Book location: {book.location}, Page we need: {book.page}")
print(book.page)

book_w = Book("Test", "Testov Test", "at the gymn")
print(book_w.page)
turn_page_w = TurnBookPage(book_w, 200)
turn_page_w.turn_page()
print(book_w.page)