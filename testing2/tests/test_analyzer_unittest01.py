from unittest.mock import Mock, patch
from analyzer import analyze_json_file


def test_analyze_json_file():
    mock_read_json_file = Mock(return_value={"name": "Carlos", "age": 33})
    fake_file_path = "invalid.json"
    with patch("analyzer.read_json_file", mock_read_json_file):
        result = analyze_json_file(fake_file_path)
    assert result == "The person's name is Carlos and the age is 33."
    mock_read_json_file.assert_called_with(fake_file_path)
