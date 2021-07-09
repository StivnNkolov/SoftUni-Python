# from Library.library import Library


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if author in library.books_available:
            if book_name in library.books_available[author]:
                self.books.append(book_name)
                library.books_available[author].remove(book_name)
                library.rented_books[self.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user_name, values in library.rented_books.items():
            if book_name in values:
                return f'The book "{book_name}" is already rented and will be available in ' \
                   f"{values[book_name]} days!"

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            if library.rented_books[self.username].get(book_name):
                library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
