# Abstraction


from abc import ABC, abstractmethod


class X(ABC):
    @abstractmethod
    def example(self) -> None:
        print("abstract method in parent class")


class Y(X):
    def example(self) -> None:
        super().example()  # calling 1st method (print statement in parent class)
        print("overriding abstract method in child class")  # calling 2nd method


if __name__ == "__main__":
    y = Y()
    y.example()
    # output:
    #   abstract method in parent class
    #   overriding abstract method in child class
