# Abstraction


from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
    
    @property  # this decorator makes the method a property
    @abstractmethod  # and this makes this property mandatory in the child class
    def name(self) -> str:
        return self._name
    
    @property
    def super_power(self) -> None | str:
        return None


class B(A):
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def super_power(self) -> str:
        return "Flying"


class C(A):
    @property
    def name(self) -> str:
        return self._name


if __name__ == "__main__":
    b = B("Superman")
    print("b super_power: ", b.super_power)
    c = C("Clark Kent")
    print("c super_power: ", c.super_power)
    # output:
    #   b super_power:  Flying
    #   c super_power:  None
