import json


def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def analyze_json_file(file_path) -> str:
    if not file_path.endswith(".json"):
        raise ValueError("The file needs to be a JSON file")
    data = read_json_file(file_path)
    return (
        f"The person's name is {data['name']} "
        f"and the age is {data['age']}."
    )
