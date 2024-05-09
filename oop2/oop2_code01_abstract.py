# Abstraction: Abstract class is a class that contains one or more abstract methods. (not only abstract methods)
# abstract method MUST be implemented in the child class, while concrete ("normal") methods aren't mandatory.
# same logic applies to abstract and concrete properties.


from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def name(self) -> None:
        pass
        # raise NotImplementedError("You must implement this method in the child class.")
        #   even without raise NotImplementedError, it will raise an error if not implemented in the child class.

    def concrete_method(self) -> None:  # not mandatory to implement in the child class
        pass


class Seller(Person):  # child class of Person
    def __init__(self, seller_name: str) -> None:
        self.seller_name = seller_name
    
    def name(self) -> None:
        print(f"Name of the seller: {self.seller_name}")