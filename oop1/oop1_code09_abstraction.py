# Abstraction


class Rectangle:
    def __init__(self, base: int | float, height: int | float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> int | float:
        return self.base * self.height

    def calculate_perimeter(self) -> int | float:
        return 2 * (self.base + self.height)


if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print("Rectangle Area: ", rectangle.calculate_area())
    print("Rectangle Perimeter: ", rectangle.calculate_perimeter())
