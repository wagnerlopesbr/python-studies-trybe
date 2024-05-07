# Mixin + Multiple Inheritance


class Animal:
    def __init__(self, name: str | None = None) -> None:
        self.name = name
    
    def make_sound(self) -> None:
        print(f"{self.name} is making a sound")


class Mammal(Animal):
    def breastfeed(self) -> None:
        print(f"{self.name} is breastfeeding")


class Dog(Mammal):
    def bark(self) -> None:
        if self.name is not None:
            print(f"'AU AU AU' - {self.name}")
        else:
            print(f"What the hell is barking?")


dog = Dog("Rex")
dog.make_sound()
dog.breastfeed()
dog.bark()
unknown_dog = Dog()
unknown_dog.make_sound()
unknown_dog.breastfeed()
unknown_dog.bark()
