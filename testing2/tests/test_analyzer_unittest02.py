from unittest.mock import Mock, patch
import pytest
from analyzer import analyze_json_file, read_json_file


def test_analyze_json_file():
    mock_read_json_file = Mock(
        side_effect=[
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25},
        ]
    )
    fake_file_patch = "invalid.json"
    with patch("analyzer.read_json_file", mock_read_json_file):
        assert (
            analyze_json_file(fake_file_patch) == "The person's name is John and the age is 30."
        )
        assert (
            analyze_json_file(fake_file_patch) == "The person's name is Jane and the age is 25."
        )
    mock_read_json_file.assert_called_with(fake_file_patch)


def test_analyze_json_file_propagates_exception():
    mock_read_json_file = Mock(side_effect=FileNotFoundError)
    fake_file_path = "invalid.json"
    with patch("analyzer.read_json_file", mock_read_json_file):
        with pytest.raises(FileNotFoundError):
            analyze_json_file(fake_file_path)


def test_read_json_file(tmp_path):
    fake_file_path = tmp_path / "file.json"
    fake_file_path.touch()
    mock_json = Mock()
    mock_json.load = Mock(return_value={"name": "John", "age": 30})
    with patch("analyzer.json", mock_json):
        result = read_json_file(fake_file_path)
    assert result == {"name": "John", "age": 30}


def test_analyze_json_file_raises_exception_when_not_json():
    fake_file_path = "invalid.txt"
    with pytest.raises(
        ValueError, match="The file needs to be a JSON file"
    ):
        analyze_json_file(fake_file_path)
