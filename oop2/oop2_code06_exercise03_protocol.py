# Protocol: A protocol is a class that defines a set of methods that a class must implement in order to implement the protocol.


from typing import Protocol


class CalculatePerimeter(Protocol):
    def calculate_perimeter(self) -> str | None:
        pass


class Square(CalculatePerimeter):
    def __init__(self, side: float | int) -> None:
        self.side = side

    def calculate_perimeter(self) -> str:
        return f"The square perimeter is {4 * self.side}."


class Triangle(CalculatePerimeter):
    def __init__(self, side1: float | int, side2: float | int, side3: float | int) -> None:
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_perimeter(self) -> str:
        return f"The triangle perimeter is {self.side1 + self.side2 + self.side3}."


if __name__ == "__main__":
    square = Square(5)
    print(square.calculate_perimeter())
    triangle = Triangle(3, 4, 5)
    print(triangle.calculate_perimeter())
    # output:
    #   The square perimeter is 20.
    #   The triangle perimeter is 12.
    # if Square or Triangle class does not implement the calculate_perimeter method, then it will raise an error. (run mypy to test it)
    # TypeError: Cannot instantiate abstract class Square/Triangle with abstract methods calculate_perimeter
