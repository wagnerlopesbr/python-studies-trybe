from abc import ABC, abstractmethod


class Customer:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone


class Address:
    def __init__(self, street: str, number: int, city: str, state: str) -> None:
        self.street = street
        self.number = number
        self.city = city
        self.state = state


def print_delivery(customer: Customer, address: Address) -> None:
    print(f"\nThe package was successfully delivered to {customer.name}")
    print(f"Address: {address.number} {address.street}, {address.city}, {address.state}")
    print(f"Phone: {customer.phone}\n")


class Deliverable(ABC):
    @abstractmethod
    def delivery(self, customer: Customer, address: Address) -> None:
        pass


class Mail(Deliverable):
    def delivery(self, customer: Customer, address: Address) -> None:
        print_delivery(customer, address)


class ShippingCompany(Deliverable):
    def delivery(self, customer: Customer, address: Address) -> None:
        print_delivery(customer, address)


def main():
    mail = Mail()
    shipping_company = ShippingCompany()
    customer = Customer("John", "123456789")
    address = Address("Main St", 123, "Springfield", "IL")
    mail.delivery(customer, address)
    shipping_company.delivery(customer, address)


if __name__ == "__main__":
    main()
