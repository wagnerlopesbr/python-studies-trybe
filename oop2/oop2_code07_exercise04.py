from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, salary: int | float) -> None:
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def calculate_bonus(self) -> str | None:
        pass


class Developer(Employee):
    def calculate_bonus(self) -> str:
        return f"Developer {self.name} bonus is {(self.salary * 1.2):.2f}."


class Analyst(Employee):
    def calculate_bonus(self) -> str:
        return f"Analyst {self.name} bonus is {(self.salary * 1.3):.2f}."


class Manager(Employee):
    def calculate_bonus(self) -> str:
        return f"Manager {self.name} bonus is {(self.salary * 1.4):.2f}."


class Worker(Employee):
    def calculate_bonus(self) -> str:
        return f"Worker {self.name} bonus is {(self.salary * 1.1):.2f}."


def main():
    developer = Developer("John", 1000)
    print(developer.calculate_bonus())
    analyst = Analyst("Jane", 1000)
    print(analyst.calculate_bonus())
    manager = Manager("Jim", 1000)
    print(manager.calculate_bonus())
    worker = Worker("Jack", 1000)
    print(worker.calculate_bonus())


if __name__ == "__main__":
    main()
