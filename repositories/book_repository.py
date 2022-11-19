from entities.book import Book


class BookRepository:
    list_books: list[Book] = []
    
    def __init__(self) -> None:
        pass

    def verif_if_book_exists(self, book_id: int) -> bool:
        for book in self.list_books:
            if (book.id == book_id):
                return True

        return False

    def get_book(self, book_id: int):
        for book in self.list_books:
            if (book.id == book_id):
                return book

        return Book(-1, "Livro não encontrado!", "", "", "", 0)
