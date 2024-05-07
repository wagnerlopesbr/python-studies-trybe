# Inheritance: A class can inherit from another class.
#              The class that inherits is called a subclass
#              and the class that is inherited from is called a superclass.

class LivingBeing:
    def __init__(self):
        self.age = 0

    def anniversary(self):
        self.age += 1


class Animal(LivingBeing):
    def __init__(self, specie: str, color: str):
        super().__init__()
        self.specie = specie
        self.color = color
    
    def eat(self, food: str):
        return f"{self.specie} is eating {food}."


class Cat(Animal):
    def __init__(
            self,
            color: str,
            have_mustache: bool,
            num_of_legs: int,
    ):
        super().__init__("Cat", color)
        self.mustache = have_mustache
        self.legs = num_of_legs
    
    def meow(self):
        return "Meow!"


mutated_cat = Cat("Black", True, 6)
print(f"print1: {mutated_cat.age}")
print(f"print2: {mutated_cat.eat('fish')}")
print(f"print3: {mutated_cat.meow()}")
mutated_cat.anniversary()
print(f"print4: {mutated_cat.age}")
