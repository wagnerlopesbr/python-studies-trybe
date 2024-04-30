import json
import os


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))


def test_generate_output(tmp_path):
    content = {"name": "Gabigol"}
    output_path = tmp_path / "out.json"
    generate_output(content, output_path)
    assert os.path.isfile(output_path)
    with open(output_path) as file:
        assert file.read() == '{"name": "Gabigol"}'
