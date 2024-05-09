from abc import ABC, abstractmethod


class Person(ABC):  # formal interface
    @abstractmethod
    def print_role(self) -> None | str:
        raise NotImplementedError


class Seller(Person):
    def print_role(self) -> None | str:
        return print("I'm a seller.")


class Manager(Person):
    def print_role(self) -> None | str:
        return print("I'm a manager.")


if __name__ == "__main__":
    seller = Seller()
    seller.print_role()
    manager = Manager()
    manager.print_role()
    # output:
    #   I'm a seller.
    #   I'm a manager.