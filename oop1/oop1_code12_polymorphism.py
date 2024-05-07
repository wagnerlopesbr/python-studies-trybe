# Polymorphism: Reusing/overriding the methods of the parent class in the child class


class Product:
    def __init__(
            self,
            name: str,
            price: int | float,
    ) -> None:
        self._name = name
        self._price = price
    
    def get_description(self) -> None:  # method to be overridden
        pass

    def get_price(self) -> None:  # method to be overridden
        pass


class Book(Product):
    def __init__(
            self,
            name: str,
            author: str,
            price: int | float,
    ) -> None:
        super().__init__(name, price)
        self._author = author
    
    def get_description(self) -> str:  # overriding the method
        return f"Book: {self._name} by {self._author}"
    
    def get_price(self) -> int | float:  # overriding the method
        return self._price


class DVD(Product):
    def __init__(
            self,
            name: str,
            direction: str,
            price: int | float,
    ) -> None:
        super().__init__(name, price)
        self._direction = direction

    def get_description(self) -> str:  # overriding the method
        return f"DVD: {self._name} by {self._direction}"
    
    def get_price(self) -> int | float:  # overriding the method
        return self._price


def print_details(product: Product) -> None:
    print(product.get_description())
    print(f"Price: {product.get_price()}")


if __name__ == "__main__":
    book = Book("The Alchemist", "Paulo Coelho", 500)
    dvd = DVD("Inception", "Christopher Nolan", 300)

    print_details(book)
    print_details(dvd)
