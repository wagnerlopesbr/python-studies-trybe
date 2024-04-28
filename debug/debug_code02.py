# THIS CODE IS ONLY FOR DEBUGGING PURPOSES
import random


DIGITS_MAP = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def separate_digits(integer: int) -> list[int]:
    digits = []
    while integer > 0:
        integer, digit = divmod(integer, 10)
        digits.append(digit)  # type: ignore
    return list(reversed(digits))  # type: ignore
    # other way to do it (ordering the digits return):
    #   return digits[::-1]  # type: ignore
    #   the line abot reverses the list:
    #       starting from the first element(:) to the last one(:), but (-1) means that it will go from the last element to the first one


def generate_int_description(integer: int):
    """Transform numbers in text"""
    # digits = [int(digit) for digit in str(integer)]
    digits = separate_digits(integer)

    description = f"{DIGITS_MAP.get(digits[0])}"
    for digit in digits[1:]:
        description += f" {DIGITS_MAP.get(digit)}"

    return description


def main():
    integer = random.randint(10000, 99999)

    description = generate_int_description(integer)

    print(f"{integer} description: '{description}'")


if __name__ == "__main__":
    main()
