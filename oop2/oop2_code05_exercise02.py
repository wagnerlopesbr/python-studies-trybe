class Product:  # informal interface
    def __init__(self, price: int | float) -> None:
        self.price = price
    
    def print_price(self) -> None | str:
        raise NotImplementedError("Subclasses must implement this method")


class Book(Product):
    def __init__(self, price: int | float) -> None:
        super().__init__(price)
    
    def print_price(self) -> None | str:
        print(f"The price of the book is {self.price}")


if __name__ == "__main__":
    book = Book(100)
    book.print_price()
    # The price of the book is 100
