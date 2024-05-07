# Encapsulation: restriction of direct access to some components.


class Blender:
    available_colors = {"RED", "BLACK", "WHITE"}
    # Getter:
    @property
    def color(self) -> str:
        return self.__color.upper()
    
    @color.setter # property_name.setter
    def color(self, new_color: str) -> None:
        if new_color.upper() not in self.available_colors:
            raise ValueError(f"{new_color} is not available")
        self.__color = new_color

    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: float | int
    ) -> None:
        self.color = color  # self.color = color will call the setter


if __name__ == "__main__":
    blender = Blender("red", 500, 220, 80)
    print(blender.color)
    blender.color = "black"
    print(blender.color)
    try:
        blender.color = "green"
    except ValueError as e:
        print(e)