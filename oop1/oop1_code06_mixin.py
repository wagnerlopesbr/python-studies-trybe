# Mixin: A class that provides methods to other classes but is not meant to be instantiated on its own.


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class FlyMixin:
    def fly(self):
        print(f"{self.name} is flying")


class Bird(Animal, FlyMixin):
    def __init__(self, name: str = "Unknown bird") -> None:
        super().__init__(name)


bird_1 = Bird("Eagle")
bird_1.fly()
bird_2 = Bird("Sparrow")
bird_2.fly()
bird_3 = Bird("Vulture")
bird_3.fly()
unknown_bird = Bird()
unknown_bird.fly()
