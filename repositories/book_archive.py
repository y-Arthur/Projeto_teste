from entities.book import Book
from repositories.book_repository import BookRepository


class BookArchive:
    file_book = list(open("books.csv", "r", encoding="utf-8"))
    book_repository = BookRepository()

    def format_str_price_to_float(price: str) -> float:
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0

    for book in file_book[1:]:
        list_book = book.split(";")
        book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                    list_book[4], format_str_price_to_float(list_book[5]))
        book_repository.list_books.append(book)
