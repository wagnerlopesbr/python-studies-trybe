class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height


    # Magic Method that returns a string representation of the object.
    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}\nHeight: {self.height}"


p1 = Person("Gabigol", 27, 1.78)
print(p1)
