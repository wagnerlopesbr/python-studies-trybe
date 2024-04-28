# THIS CODE IS ONLY FOR DEBUGGING PURPOSES
from math import factorial


def map_factorial(numbers_list: list[int]) -> list[int]:
    result = []
    for num in numbers_list:
        result.append(factorial(num))  # type: ignore
    return result  # type: ignore


def main() -> list[int]:
    input_list = [4, 2, 3, 1, 5]
    return map_factorial(input_list)


def inverse_factorial(number: int):
    num = 1
    target_factorial = 1
    while num < number:
        target_factorial += 1
        num *= target_factorial
    if num == number:
        return target_factorial
    return None


if __name__ == "__main__":
    final_result = main()
    for r in final_result:
        print(f"the {inverse_factorial(r)} factorial is: {r}")
