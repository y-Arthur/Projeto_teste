from entities.book import Book
from repositories.book_repository import BookRepository


class BookArchive:
    def __init__(self, book_repository: BookRepository) -> None:
        self.file_book = list(open("books.csv", "r", encoding="utf-8"))
        self.book_repository = book_repository

    def format_str_price_to_float(self, price: str) -> float:
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0

    def init_book_repository(self):
        for book in self.file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                        list_book[4], self.format_str_price_to_float(list_book[5]))
            self.book_repository.list_books.append(book)
