from analyzer import analyze_json_file


def test_analyze_json_file():
    result = analyze_json_file("person_data.json")
    assert result == "The person's name is John and the age is 30."