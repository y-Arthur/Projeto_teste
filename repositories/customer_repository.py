from entities.customer import Customer


class CustomerRepository:
    list_customers: list[Customer] = []
    
    def __init__(self) -> None:
        pass
    
    def verif_if_customer_exists(self, customer_id: int) -> bool:
        for customer in self.list_customers:
            if (customer.id == customer_id):
                return True

        return False

    def get_customer(self, customer_id: int) -> Customer:
        for customer in self.list_customers:
            if (customer.id == customer_id):
                return customer

        return Customer(-1, "Cliente não encontrado!")
