from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class MobileFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:10]


class BrowserFormatter(Formatter):
    def format(self, book: Book):
        return book.content[:5]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


test_book = Book("123456789101112131415")
mobile_formatter = MobileFormatter()
browser_formatter = BrowserFormatter()

test_printer = Printer()
print(test_printer.get_book(test_book, browser_formatter))
