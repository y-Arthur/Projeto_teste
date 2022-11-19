from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.book_repository import BookRepository
from repositories.book_archive import BookArchive
from entities.order import Order


class UserInterface:
    def __init__(self) -> None:
        self.customer_repository = CustomerRepository()
        self.order_repository = OrderRepository()
        self.book_repository = BookRepository()
        self.book_archive = BookArchive(self.book_repository)

    def verif_if_customer_exists(self, customer_id: int) -> bool:
        return self.customer_repository.verif_if_customer_exists(customer_id)
    
    def get_customer(self, customer_id: int):
        return self.customer_repository.get_customer(customer_id)

    def set_order(self, order: Order) -> None:
        self.order_repository.set_order(order)   

    def verif_if_book_exists(self, book_id: int) -> bool:
        return self.book_repository.verif_if_book_exists(book_id)
    
    def get_book(self, book_id: int):
        return self.book_repository.get_book(book_id)

    def init_book_repository(self) -> None:
        self.book_archive.init_book_repository()

    def principal_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0
