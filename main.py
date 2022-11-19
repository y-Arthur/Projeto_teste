from datetime import date

from entities.customer import Customer
from entities.order import Order
from user_interface import UserInterface


user_interface = UserInterface()
user_interface.init_book_repository()

while True:
    menu_option = user_interface.principal_menu()
    if (menu_option == 0):
        break

    print("\n")

    if menu_option == 1:
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        customer = Customer(id, nome)
        user_interface.customer_repository.list_customers.append(customer)
        print("Client cadastrado com sucesso!")
    if menu_option == 2:
        id = int(input("Informe o código do pedido: "))
        customer_id = int(input("Informe o código do cliente: "))
        today = date.today()
        if (not user_interface.verif_if_customer_exists(customer_id)):
            print("Cliente não existe!")
            continue

        customer = user_interface.get_customer(customer_id)
        book_id = int(input("Informe o código do livro: "))

        if (not user_interface.verif_if_book_exists(book_id)):
            print("Livro não existe!")
            continue

        book = user_interface.get_book(book_id)
        order = Order(id, customer, today)
        order.purchased_book = book

        user_interface.order_repository.list_orders.append(order)
        print("Pedido cadastrado com sucesso!")
    if menu_option == 3:
        print("\n***** Relatório de pedidos *****\n")
        for order in user_interface.order_repository.list_orders:
            print(f"Código do Pedido: {order.id}")
            print(f"Cliente: {order.customer.name}")
            print(f"Data do pedido: {order.date_order}")
            print(f"Livro escolhido: {order.purchased_book.name} \n")
    if menu_option == 4:
        formatText = "{0:<10} {1:<20}\n"
        menu = ("\n***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in user_interface.customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)
    if menu_option == 5:
        formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Ttítulo", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")

        for book in user_interface.book_archive.book_repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)
