# Composition: Car and Motorcycle are vehicles, so Vehicle is a superclass of Car and Motorcycle and composes them.

class Vehicle:
    def __init__(
            self,
            name: str,
            capacity: int,
    ) -> None:
        self.name = name
        self.capacity = capacity
    
    def move(self, distance: int) -> str:
        return (
            f"{self.name} "
            f"carried {self.capacity} people "
            f"across {distance} kilometers."
        )
        

class Car(Vehicle):
    def move(self, distance: int) -> str:
        return f"Car {super().move(distance)}"


class Motorcycle(Vehicle):
    def __init__(self, name: str) -> None:
        self.name = name
        self.capacity = 2


car = Car("Gol", 5)
motorcycle = Motorcycle("CG 125")
print(car.move(100))
print(motorcycle.move(100))
