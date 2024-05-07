from abc import ABC, abstractmethod
from math import pi as PI


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError  # method must be implemented in the subclass, otherwise it will raise an error
    
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side: int | float) -> None:
        self.__side = side
    
    def area(self) -> int | float:
        return self.__side * self.__side

    def perimeter(self) -> int | float:
        return 4 * self.__side


class Rectangle(Shape):
    def __init__(self, base: int | float, height: int | float) -> None:
        self.__base = base
        self.__height = height
    
    def area(self) -> int | float:
        return self.__base * self.__height

    def perimeter(self):
        return 2 * (self.__base + self.__height)


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.__radius = radius
    
    def area(self) -> int | float:
        return PI * (self.__radius ** 2)

    def perimeter(self) -> int | float:
        return 2 * PI * self.__radius



if __name__ == "__main__":
    square = Square(5)
    print("Square area: ", square.area())
    print("Square perimeter: ", square.perimeter())

    rectangle = Rectangle(5, 10)
    print("Rectangle area: ", rectangle.area())
    print("Rectangle perimeter: ", rectangle.perimeter())

    circle = Circle(5)
    print("Circle area: ", circle.area())
    print("Circle perimeter: ", circle.perimeter())


    # ERROR SCENARIOS
    # shape = Shape()  
    #   TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

    # square = Square(5)
    #   TypeError: Can't instantiate abstract class Square with abstract methods area, perimeter

    # rectangle = Rectangle(5, 10)
    #   TypeError: Can't instantiate abstract class Rectangle with abstract methods area, perimeter

    # circle = Circle(5)
    #   TypeError: Can't instantiate abstract class Circle with abstract methods area, perimeter
