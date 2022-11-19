from entities.order import Order


class OrderRepository:
    list_orders: list[Order] = []
    
    def _init_(self) -> None:
        pass

    def set_order(self, order: Order) -> None:
        self.list_orders.append(order)

    def get_total_price(self, order: Order) -> float:
        for item in self.list_orders:
            if (order.id == item.id):
                return item.total_price
        return 0

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}\n"
        orders = ("\n***** Relatório de pedidos *****\n")
        orders += formatText.format("Código", "Cliente", "Data", "Livro", "Preço Total")

        for order in self.list_orders:
            orders += formatText.format(order.id, order.customer.name, f"{order.date_order}", order.purchased_book.name, f"R$ {order.total_price}")

        return orders
