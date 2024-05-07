# Composition: HomeAppliance is a superclass of Blender and composes it.

from typing import List

class HomeAppliance:
    def __init__(
        self, color: str, power: int, voltage: int, price: float | int
    ) -> None:
        self.color = color
        self.price = price
        self.power = power
        self.voltage = voltage
        self.max_speed = 3
        self.turn_off()
    
    def turn_on(self, speed: int) -> None:
        self.is_on = True 
        self.speed = speed if speed <= self.max_speed else self.max_speed

    def turn_off(self) -> None:
        self.is_on = False
        self.speed = 0


class Blender(HomeAppliance):
    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: float | int
    ) -> None:
        super().__init__(color, power, voltage, price)
        self.max_speed = 4


class Person:
    def __init__(self, name: str, money: float | int) -> None:
        self.name = name
        self.money = money
        self.homeappliances: List[HomeAppliance] = []
    
    def buy_blender(self, homeappliance: HomeAppliance) -> None:
        if self.money >= homeappliance.price:
            self.money -= homeappliance.price
            self.homeappliances.append(homeappliance)
        else:
            print("Not enough money")

    def get_homeappliances(self) -> List[HomeAppliance]:
        return self.homeappliances

if __name__ == "__main__":
    person = Person("John", 400)
    print(f"person money: {person.money}")
    blender_1 = Blender("red", 500, 220, 80)
    person.buy_blender(blender_1)
    print(f"person money: {person.money}")
    print(f"person homeappliance: {person.get_homeappliances()}")
    blender_2 = Blender("blue", 600, 220, 90)
    person.buy_blender(blender_2)
    print(f"person money: {person.money}")
    print(f"person homeappliance: {person.get_homeappliances()}")
    blender_3 = Blender("green", 700, 220, 300)
    person.buy_blender(blender_3)
    print(f"person money: {person.money}")
    print(f"person homeappliance: {person.get_homeappliances()}")
