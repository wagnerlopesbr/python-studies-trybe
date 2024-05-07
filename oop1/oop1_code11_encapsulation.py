# Encapsulation


class MonthlyExpense:
    __slots__ = ["internet", "grocery", "_power", "_water", "__rent"]
    def __init__(
            self,
            internet: int | float,
            grocery: int | float,
            power: int | float,
            water: int | float,
            rent: int | float,
    ) -> None:
        self.internet = internet
        self.grocery = grocery
        self._power = power
        self._water = water
        self.__rent = rent
    
    def get_rent(self) -> int | float:
        return self.__rent

    def get_power(self) -> int | float:
        return self._power

    def set_power(self, new_power: int | float) -> None:
        self._power = new_power
    
    def get_water(self) -> int | float:
        return self._water
    
    def set_water(self, new_water: int | float) -> None:
        self._water = new_water


if __name__ == "__main__":
    expenses = MonthlyExpense(50, 200, 100, 30, 500)
    print("Internet: ", expenses.internet, "$")
    print("Grocery: ", expenses.grocery, "$")
    print("Power: ", expenses.get_power(), "$")
    print("Water: ", expenses.get_water(), "$")
    try:
        print(expenses.__rent)
    except AttributeError as e:
        print("Error! There is no value: ", e)
    expenses.set_power(150)
    expenses.set_water(40)
    print("New Power: ", expenses.get_power(), "$")
    print("New Water: ", expenses.get_water(), "$")
    expenses.qlqrporra = 600
    print("Rent: ", expenses.qlqrporra)
    print("Rent: ", expenses.get_rent(), "$")
