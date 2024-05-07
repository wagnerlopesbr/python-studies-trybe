# Abstraction: is the process of hiding the implementation details and showing only the functionality to the user.


from oop1_code04_composition import Blender


if __name__ == "__main__":
    red_blender = Blender("Red", 1000, 110, 220)
    red_blender.turn_on(1)  # abstracted method
    print("Is the blender on? ", red_blender.is_on)
    red_blender.turn_off()  # abstracted method
    print("Is the blender on? ", red_blender.is_on)
